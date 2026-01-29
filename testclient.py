# I want to call http://localhost:8888/generate with a JSON body, and save the result as a PPTX file.
import requests
def main():
    url = "http://localhost:8888/dynamic"
    json_data = {
        "template": "/code/app/templates/template2.pptx",
        "slides": [
            {
                "title": "Dynamic Slide Title"
            },
            {
                "title": "Agenda",
                "content": ["* Introduction\n* Main Topic\n* Conclusion"]
            },
            {
                "title": "Intro - Test Client",
                "pictures": [
                    "https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/media/managed-virtual-network/diagram-managed-network.png?view=foundry-classic"
                ]
            },
            {
                "title": "Some Topic"
            },
            {

                "title": "We can now generate slides!",
                "content": ["We take a template PPTX with placeholders and fill them with data using Jinja2 templating."],
                "pictures": [
                   "https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/Content-Card-Xbox-Controllers-Black-Detail"
                ]
            },
            {
                "title": "Comparison to Version 2",
                "text": ["version1", "version2"],
                "content": [
                    "Jinja2 templating\nstatic page count",
                    "Dynamic slide count\nmore flexible"
                ]
            },
            {
                "title": "Conclusion",
                "content": ["This is the conclusion slide."],
                "tables": [
                    { 
                        "headers": ["Year", "Earnings", "Profit"],
                        "rows": [
                            ["2023", 10000000, 2000000],
                            ["2024", 25000000, 4000000],
                            ["2025", 35000000, 6000000]
                        ]
                    }
                ]
            },
            {
                "title": "Thank you for your attention!",
                "subtitles": [
                    "Test Bot\n- test@nothing.com\n- 555-123-4567"
                ]
            }
        ]
    }
    
#     json_data = {
#     "template": "/code/app/templates/template.pptx",
#     "slides": [
#         {
#             "title": "Star Wars is Cool"
#         },
#         {
#             "agenda": [
#                 "Introduction",
#                 "What makes Star Wars cool?",
#                 "Iconic characters & ships",
#                 "Star Wars art & fandom",
#                 "Conclusion"
#             ]
#         },
#         {
#             "title": "Introduction - The Star Wars Universe",
#             "pictures": [
#                 "https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=800&q=80"
#             ]
#         },
#         {
#             "sectionname": "What Makes Star Wars Cool?"
#         },
#         {
#             "title": "Why Fans Love Star Wars",
#             "content": "Star Wars combines epic storytelling, creative world-building, memorable characters, and legendary battles between good and evil. Its influence spans movies, TV, games, art, and more.",
#             "pictures": [
#                 "https://lumiere-a.akamaihd.net/v1/images/607598d0230e6a00018e21b2-image_354b1b56.jpeg?region=0%2C48%2C1536%2C768"
#             ]
#         },
#         {
#             "title": "Iconic Characters & Ships",
#             "content": "Star Wars is renowned for its legendary cast: Luke Skywalker, Darth Vader, Princess Leia, Yoda, and more. The Millennium Falcon, X-Wings, and Star Destroyers are pop-culture icons.",
#             "tables": [
#                 {
#                     "headers": ["Character", "Role", "First Appearance"],
#                     "rows": [
#                         ["Luke Skywalker", "Hero", "A New Hope"],
#                         ["Darth Vader", "Villain", "A New Hope"],
#                         ["Princess Leia", "Rebel Leader", "A New Hope"]
#                     ]
#                 }
#             ]
#         },
#         {
#             "thanks": "Thank you for celebrating Star Wars!",
#             "contactinfo": "Test Bot\n- test@nothing.com\n- 555-123-4567"
#         }
#     ]
# }
    response = requests.post(url, json=json_data)
    if response.status_code == 200:
        # with open("generated_presentation.pptx", "wb") as f:
        #     f.write(response.content)
        # print("PPTX file saved as generated_presentation.pptx")
        print(response.json())
    else:
        print(f"Failed to generate PPTX. Status code: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    main()