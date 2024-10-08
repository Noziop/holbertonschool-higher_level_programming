#!/usr/bin/python3
''' Module that fetches data from an API '''

import requests
import csv

def fetch_and_print_posts():
    ''' Fetches data from an API and prints post titles '''
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print(f'Status Code: {response.status_code}')
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))

def fetch_and_save_posts():
    ''' Fetches data from an API and saves it to a CSV file '''
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        with open('posts.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['userId', 'id', 'title', 'body'])
            writer.writeheader()
            for post in posts:
                writer.writerow({
                    'userId': post.get('userId'),
                    'id': post.get('id'),
                    'title': post.get('title'),
                    'body': post.get('body')
                })
        print('Data saved to posts.csv')
    else:
        print(f'Failed to fetch posts. Status Code: {response.status_code}')

if __name__ == '__main__':
    fetch_and_print_posts()
    fetch_and_save_posts()