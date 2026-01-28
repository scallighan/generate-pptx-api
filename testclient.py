# I want to call http://localhost:8888/generate with a JSON body, and save the result as a PPTX file.
import requests
def main():
    url = "http://localhost:8888/generate"
    json_data = {
        "template": '/code/app/templates/template.pptx',
        "slides": [
            {
                "title": "Dynamic Slide Title"
            },
            {
                "agenda": [
                    "Intros",
                    "Some Topic",
                    "Conclusion"
                ]
            },
            {
                "title": "Intro - Test Client",
                "pictures": [
                    "https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/media/managed-virtual-network/diagram-managed-network.png?view=foundry-classic"
                ]
            },
            {
                "sectionname": "Some Topic",
            },
            {

                "title": "We can now generate slides!",
                "content": "We take a template PPTX with placeholders and fill them with data using Jinja2 templating.",
                "pictures": [
                   "https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/Content-Card-Xbox-Controllers-Black-Detail"
                ]
            },
            {
                "title": "Conclusion",
                "content": "This is the conclusion slide.",
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
                "thanks": "Thank you for your attention!",
                "contactinfo": "Test Bot\n- test@nothing.com\n- 555-123-4567"
            }
        ]
    }
    response = requests.post(url, json=json_data)
    if response.status_code == 200:
        with open("generated_presentation.pptx", "wb") as f:
            f.write(response.content)
        print("PPTX file saved as generated_presentation.pptx")
    else:
        print(f"Failed to generate PPTX. Status code: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    main()