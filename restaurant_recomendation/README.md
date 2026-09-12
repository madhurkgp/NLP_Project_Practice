# Restaurant Recommendation System

A location-based restaurant recommendation system using K-Means clustering on Yelp dataset data for Las Vegas restaurants.

## Overview

This system analyzes restaurant locations in Las Vegas and provides personalized recommendations based on geographic proximity. It uses machine learning clustering to group restaurants by location and recommends top-rated restaurants within the same cluster as the user's location.

## Features

- **Location-based Recommendations**: Get restaurant suggestions based on your geographic coordinates
- **K-Means Clustering**: Groups restaurants into geographic clusters for efficient recommendation
- **Interactive Interface**: Command-line interface for getting recommendations
- **Data Visualization**: Visualize restaurant clusters on maps
- **Comprehensive Analysis**: Includes exploratory data analysis and performance metrics

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Setup

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd restaurant_recomendation
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the dataset:
   ```bash
   python download_data.py
   ```

## Usage

### Running the Complete Analysis

To run the full analysis pipeline including data loading, clustering, and example recommendations:

```bash
python restaurant_recommendation.py
```

This will:
- Load and filter the Yelp dataset
- Perform exploratory data analysis
- Determine optimal number of clusters using the elbow method
- Train the K-Means clustering model
- Show example recommendations for test locations
- Launch an interactive recommendation interface

### Getting Recommendations

After running the main script, you can enter coordinates to get personalized restaurant recommendations:

```
Enter longitude (e.g., -115.1891691): -115.1891691
Enter latitude (e.g., 36.1017316): 36.1017316
```

The system will return the top 5 restaurants in your area, sorted by rating and review count.

### Example Locations

Here are some example coordinates for Las Vegas areas:

- **Downtown Las Vegas**: Longitude: -115.1891691, Latitude: 36.1017316
- **Summerlin**: Longitude: -115.2798544, Latitude: 36.0842838  
- **Henderson**: Longitude: -115.082821, Latitude: 36.155011

## Project Structure

```
restaurant_recomendation/
├── restaurant_recommendation.py    # Main application script
├── download_data.py               # Dataset downloader
├── requirements.txt              # Python dependencies
├── README.md                      # This file
└── yelp_academic_dataset_business.json  # Dataset (downloaded)
```

## How It Works

1. **Data Loading**: Loads the Yelp business dataset and filters for restaurants in Las Vegas
2. **Feature Engineering**: Extracts geographic coordinates (latitude, longitude)
3. **Clustering**: Uses K-Means to group restaurants into geographic clusters
4. **Recommendation**: When given user coordinates, finds the nearest cluster and recommends top-rated restaurants within that cluster
5. **Ranking**: Restaurants are ranked by star rating and review count

## Algorithm Details

### K-Means Clustering
- Uses geographic coordinates (longitude, latitude) as features
- Determines optimal number of clusters using the elbow method
- Evaluates clustering quality with silhouette score
- Default: 5 clusters for Las Vegas area

### Recommendation Logic
1. Predict cluster for user's coordinates
2. Filter restaurants in the same cluster
3. Sort by star rating (descending) and review count (descending)
4. Return top N recommendations

## Dependencies

- `pandas`: Data manipulation and analysis
- `numpy`: Numerical computing
- `scikit-learn`: Machine learning algorithms (K-Means clustering)
- `matplotlib`: Data visualization
- `seaborn`: Statistical data visualization
- `plotly`: Interactive visualizations
- `requests`: HTTP requests for data download

## Dataset

This project uses the Yelp Academic Dataset, specifically the business data containing:
- Restaurant information (name, location, categories)
- User ratings and review counts
- Geographic coordinates

The dataset is automatically downloaded when running `download_data.py`.

## Performance

- **Dataset Size**: ~192K businesses, ~59K restaurants
- **Las Vegas Restaurants**: ~10K+ restaurants
- **Clustering**: Optimized for 5 clusters with silhouette score ~0.39
- **Recommendation Speed**: Real-time recommendations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Potential Improvements

- **Additional Features**: Incorporate cuisine type, price range, hours of operation
- **Advanced Algorithms**: Try DBSCAN or hierarchical clustering for better geographic grouping
- **User Preferences**: Add personalization based on user history and preferences
- **Real-time Data**: Integrate with live Yelp API for up-to-date information
- **Web Interface**: Build a web application with interactive maps
- **Mobile App**: Create a mobile application for on-the-go recommendations

## License

This project is for educational purposes. Please respect the Yelp dataset terms of service.

## Troubleshooting

### Common Issues

1. **Dataset Download Fails**: 
   - Check internet connection
   - Try running `download_data.py` manually
   - Manually download from Yelp if needed

2. **Import Errors**:
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version compatibility

3. **Memory Issues**:
   - Dataset is large (~23MB when compressed)
   - Ensure sufficient RAM available

4. **Visualization Issues**:
   - Plotly visualizations may not display in all environments
   - Try running in Jupyter notebook for best visualization experience

### Getting Help

If you encounter issues:
1. Check this README for solutions
2. Ensure all dependencies are properly installed
3. Verify the dataset is downloaded and accessible
4. Check Python and package versions

## Authors

This project was created as part of a machine learning and data science learning journey.

## Acknowledgments

- Yelp for providing the academic dataset
- Scikit-learn for the machine learning algorithms
- Plotly for interactive visualization tools
