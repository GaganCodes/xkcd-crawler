import requests

# Drafting JSON request
comic_range = range(1,50)

for i in comic_range:
    print("Comic Number: ", i)
    request_xkcd = requests.get("https://xkcd.com/{}/info.0.json".format(i))

    # Checking if response is OK (return code = 200)
    if request_xkcd.status_code == 200:
        # Convert response to JSON
        response = request_xkcd.json()
        # Get the specific .png URL
        img = requests.get(response["img"])

        image_file = open("xkcd_{}.PNG".format(response["num"]), "wb")
        # Getting the raw binary content for the image
        # Reference: https://requests.readthedocs.io/en/latest/api/#requests.Response
        # Property request.content
        image_file.write(img.content)
        image_file.close()