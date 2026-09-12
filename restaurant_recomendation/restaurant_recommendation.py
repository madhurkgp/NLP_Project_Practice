import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import os
import warnings

warnings.filterwarnings('ignore')

class RestaurantRecommendationSystem:
    def __init__(self):
        self.df = None
        self.df_restaurants = None
        self.las_vegas_restaurants = None
        self.kmeans = None
        self.data_file = 'yelp_academic_dataset_business.json'
        
    def load_data(self):
        """Load the Yelp dataset"""
        if not os.path.exists(self.data_file):
            print(f"Error: {self.data_file} not found. Please download the dataset first.")
            return False
            
        print("Loading dataset...")
        self.df = pd.read_json(self.data_file, lines=True)
        print(f"Dataset loaded with {self.df.shape[0]} businesses")
        return True
        
    def filter_restaurants(self):
        """Filter for restaurants only"""
        print("Filtering restaurants...")
        self.df['Restaurants'] = self.df['categories'].str.contains('Restaurants', na=False)
        self.df_restaurants = self.df.loc[self.df.Restaurants == True].copy()
        print(f"Found {self.df_restaurants.shape[0]} restaurants")
        
    def filter_las_vegas(self):
        """Filter for Las Vegas restaurants"""
        print("Filtering Las Vegas restaurants...")
        self.las_vegas_restaurants = self.df_restaurants[self.df_restaurants.state == 'NV'].copy()
        print(f"Found {self.las_vegas_restaurants.shape[0]} restaurants in Las Vegas")
        
    def determine_optimal_clusters(self, max_k=25):
        """Determine optimal number of clusters using elbow method"""
        print("Determining optimal number of clusters...")
        coords = self.las_vegas_restaurants[['longitude', 'latitude']]
        
        distortions = []
        K = range(1, max_k + 1)
        
        for k in K:
            kmeans_model = KMeans(n_clusters=k, random_state=42, n_init=10)
            kmeans_model = kmeans_model.fit(coords)
            distortions.append(kmeans_model.inertia_)
            
        # Plot elbow method
        plt.figure(figsize=(12, 8))
        plt.plot(K, distortions, marker='o')
        plt.xlabel('Number of clusters (k)')
        plt.ylabel('Distortions')
        plt.title('Elbow Method For Optimal k')
        plt.grid(True)
        plt.savefig('elbow_method.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return distortions
        
    def train_clustering_model(self, n_clusters=5):
        """Train K-means clustering model"""
        print(f"Training K-means model with {n_clusters} clusters...")
        coords = self.las_vegas_restaurants[['longitude', 'latitude']]
        
        self.kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42, n_init=10)
        self.kmeans.fit(coords)
        
        # Add cluster labels to dataframe
        self.las_vegas_restaurants['cluster'] = self.kmeans.predict(coords)
        
        # Calculate silhouette score
        score = silhouette_score(coords, self.kmeans.labels_, metric='euclidean')
        print(f"Silhouette score: {score:.4f}")
        
        return score
        
    def get_top_restaurants(self, n_top=20):
        """Get top restaurants by review count and stars"""
        return self.las_vegas_restaurants.sort_values(
            by=['review_count', 'stars'], 
            ascending=False
        ).head(n_top)
        
    def recommend_restaurants(self, longitude, latitude, n_recommendations=5):
        """
        Recommend restaurants based on location
        
        Args:
            longitude (float): User's longitude
            latitude (float): User's latitude  
            n_recommendations (int): Number of recommendations to return
            
        Returns:
            DataFrame: Top n restaurants in the same cluster
        """
        if self.kmeans is None:
            raise ValueError("Model not trained. Please train the model first.")
            
        # Predict the cluster for the given coordinates
        cluster = self.kmeans.predict(np.array([longitude, latitude]).reshape(1, -1))[0]
        
        # Get restaurants in the same cluster, sorted by rating and review count
        cluster_restaurants = self.las_vegas_restaurants[
            self.las_vegas_restaurants['cluster'] == cluster
        ].copy()
        
        recommendations = cluster_restaurants.sort_values(
            by=['stars', 'review_count'], 
            ascending=False
        ).head(n_recommendations)
        
        return recommendations[['name', 'stars', 'review_count', 'latitude', 'longitude', 'address']]
        
    def visualize_clusters(self, zoom=10):
        """Visualize restaurant clusters on a map"""
        if self.las_vegas_restaurants is None or 'cluster' not in self.las_vegas_restaurants.columns:
            print("Error: No clustering results available. Please train the model first.")
            return
            
        print("Creating cluster visualization...")
        
        # Create scatter mapbox
        fig = px.scatter_mapbox(
            self.las_vegas_restaurants,
            lat="latitude", 
            lon="longitude", 
            color="cluster",
            size='review_count',
            hover_data=['name', 'stars', 'review_count'],
            zoom=zoom, 
            width=1200, 
            height=800,
            title="Las Vegas Restaurant Clusters"
        )
        
        fig.update_layout(mapbox_style="open-street-map")
        fig.show()
        
    def run_analysis(self):
        """Run the complete analysis pipeline"""
        print("=" * 50)
        print("Restaurant Recommendation System Analysis")
        print("=" * 50)
        
        # Load and filter data
        if not self.load_data():
            return
            
        self.filter_restaurants()
        self.filter_las_vegas()
        
        # Show dataset statistics
        print("\nDataset Statistics:")
        print(f"Total businesses: {self.df.shape[0]}")
        print(f"Total restaurants: {self.df_restaurants.shape[0]}")
        print(f"Las Vegas restaurants: {self.las_vegas_restaurants.shape[0]}")
        
        # Show top restaurants
        print("\nTop 10 Restaurants in Las Vegas:")
        top_restaurants = self.get_top_restaurants(10)
        print(top_restaurants[['name', 'stars', 'review_count']].to_string(index=False))
        
        # Determine optimal clusters
        self.determine_optimal_clusters()
        
        # Train model
        self.train_clustering_model(n_clusters=5)
        
        # Show example recommendations
        print("\nExample Recommendations:")
        test_locations = [
            (-115.1891691, 36.1017316),  # Downtown Las Vegas
            (-115.2798544, 36.0842838),  # Summerlin
            (-115.082821, 36.155011)     # Henderson
        ]
        
        for i, (lon, lat) in enumerate(test_locations, 1):
            print(f"\nLocation {i} (Lon: {lon}, Lat: {lat}):")
            recommendations = self.recommend_restaurants(lon, lat, 3)
            for _, restaurant in recommendations.iterrows():
                print(f"  - {restaurant['name']} (⭐ {restaurant['stars']}, {restaurant['review_count']} reviews)")
        
        print("\nAnalysis complete!")
        print("Use the recommend_restaurants() method to get recommendations for any location.")

def main():
    """Main function to run the restaurant recommendation system"""
    # Initialize the system
    recommender = RestaurantRecommendationSystem()
    
    # Run complete analysis
    recommender.run_analysis()
    
    # Interactive recommendation example
    print("\n" + "=" * 50)
    print("Interactive Restaurant Recommendations")
    print("=" * 50)
    
    while True:
        try:
            print("\nEnter coordinates for restaurant recommendations:")
            print("Example: Downtown Las Vegas area")
            longitude = float(input("Enter longitude (e.g., -115.1891691): "))
            latitude = float(input("Enter latitude (e.g., 36.1017316): "))
            
            recommendations = recommender.recommend_restaurants(longitude, latitude, 5)
            
            print(f"\nTop 5 restaurant recommendations for your location:")
            print("-" * 60)
            for i, (_, restaurant) in enumerate(recommendations.iterrows(), 1):
                print(f"{i}. {restaurant['name']}")
                print(f"   Rating: ⭐ {restaurant['stars']}/5.0")
                print(f"   Reviews: {restaurant['review_count']}")
                print(f"   Address: {restaurant['address']}")
                print()
            
            continue_input = input("Get recommendations for another location? (y/n): ").lower()
            if continue_input != 'y':
                break
                
        except ValueError:
            print("Invalid input. Please enter valid numerical coordinates.")
        except Exception as e:
            print(f"Error: {e}")
            break
    
    print("Thank you for using the Restaurant Recommendation System!")

if __name__ == "__main__":
    main()
