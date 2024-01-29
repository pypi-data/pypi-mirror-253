import requests
import os

def update(API_URL, key, image_file_paths, new_key = None):
    files = [("updated_files", (os.path.basename(image_path), open(image_path, "rb"))) for image_path in image_file_paths]
    data = {"new_key": new_key}

    try:
        response = requests.put(f"{API_URL}/update/{key}", files=files, data=data)

        if response.status_code == 200:
            print("Update successful:", response.json())
        else:
            raise requests.HTTPError(response.text)

    except requests.HTTPError as e:
        print("Error:", e)

def delete(API_URL, key):
    try:
        response = requests.delete(f"{API_URL}/delete/{key}")
        response.raise_for_status()

        data = response.json()
        print(data["message"])
    except requests.exceptions.RequestException as error:
        print("Error deleting image:", error)
