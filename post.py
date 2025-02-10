import requests

class Post:
    def __init__(self):
        self.blog_url = 'https://api.npoint.io/f816da860f0b8485e79f'

    def blog(self):
        blog_response = requests.get(url=self.blog_url)
        blog_response.raise_for_status()
        blog_data = blog_response.json()
        return blog_data