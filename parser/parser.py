import requests


class Parsing:
    BASE_URL = 'https://coursive.id/api/v1/courses'

    def get_response(self, link):
        response = requests.get(link)
        response_json = response.json()
        return response_json

    def parse(self):
        data_list = []
        courses_list_response = self.get_response(self.BASE_URL)
        for i in courses_list_response['results']:
            id_ = i['id']
            title = i['title']
            image = i['image']
            slug = i['slug']

            details_response = self.get_response(f"{self.BASE_URL}/{slug}")

            youtube_url = details_response['youtube']
            blocks = details_response['blocks']

            data_list.append(
                {
                    'course_id': id_,
                    'title': title,
                    'image': image,
                    'slug': slug,
                    'youtube url': youtube_url,
                    'blocks': blocks
                }
            )
        return data_list


list_of_data = Parsing().parse()
Course.create_from_list(list_of_data)