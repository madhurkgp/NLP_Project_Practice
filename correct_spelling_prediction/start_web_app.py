#!/usr/bin/env python3
"""
Startup script for the Django spelling correction web application
"""

import os
import sys
import subprocess

def main():
    """Start the Django web application."""
    print("=== Starting Spelling Correction Web Application ===")
    
    # Change to the Django project directory
    django_dir = os.path.join(os.path.dirname(__file__), 'code', 'mysite')
    os.chdir(django_dir)
    
    print(f"Working directory: {os.getcwd()}")
    
    # Check if requirements are installed
    try:
        import django
        print(f"Django version: {django.get_version()}")
    except ImportError:
        print("Django not found. Installing requirements...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    
    # Run migrations
    print("Running database migrations...")
    subprocess.run([sys.executable, 'manage.py', 'migrate'])
    
    # Start the development server
    print("\nStarting Django development server...")
    print("Open your browser and go to: http://127.0.0.1:8000/")
    print("Press Ctrl+C to stop the server.\n")
    
    subprocess.run([sys.executable, 'manage.py', 'runserver'])

if __name__ == "__main__":
    main()
