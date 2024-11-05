# import requests
# import json
#
#
# def image_save(times):
#     for i in range(times):
#         result = requests.get("https://api.thedogapi.com/v1/images/search")
#         res_text = json.loads(result.text)
#         res_url = res_text[0]["url"]
#         res_image = requests.get(res_url)
#         with open(f"{i+1}_dog.jpg", "wb") as f:
#             f.write(res_image.content)
#
#
# print(image_save(int(input("Enter n"))))

from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
print(type(soup))
print(soup.body)
