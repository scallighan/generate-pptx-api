from fastapi import FastAPI, Query, Header, Request, Body
from fastapi.responses import FileResponse
from typing import Union, Any
from pptx import Presentation
from pptx.enum.shapes import PP_PLACEHOLDER_TYPE
from jinja2 import Template, exceptions
import json
import httpx
import re
import time

app = FastAPI(
    title="Generate PPTX API",
)

@app.get(
    "/hello",
    tags=["APIs"],
    response_model=dict,
)
async def hello(prompt: Union[str, None] = Query(default="world", max_length=50)):
    print(f"Received prompt: {prompt}")
    return {"message": f"Hello, {prompt}!"}

@app.get(
    "/read",
    tags=["APIs"],
    response_model=dict,
)
async def read_pptx():
    prs = Presentation('/code/app/templates/template.pptx')
    for slide in prs.slides:
        # for shape in slide.shapes:
        #     if shape.has_text_frame:
        #         print(repr(shape.text))
        print(f"Slide id: {slide.slide_id}")
        print(f"Slide Name: {slide.name}")
        print(f"Slide Layout: {slide.slide_layout}")
        print(f"Slide Placeholders:")
        for placeholder in slide.placeholders:
            print(f"    Placeholder name: {placeholder.name}")
            print(f"        type: {placeholder.placeholder_format.type},") 
            print(f"        has_text_frame: {placeholder.has_text_frame},")
            print(f"        text: {placeholder.text}, ")
            print(f"        shape_id: {placeholder.shape_id} ")
            
    return {"message": "PPTX content read successfully."}

async def generate_pptx(data: Any) -> str:
    template = data.get("template", "/code/app/templates/template.pptx")
    prs = Presentation(template)

    for i in range(len(prs.slides)):
        images_index = 0
        tables_index = 0
        slide = prs.slides[i]
        slide_data = data["slides"][i]
        for placeholder in slide.placeholders:
            if placeholder.has_text_frame:
                template = Template(placeholder.text)
                output = template.render(slide_data)
                print(repr(output))
                placeholder.text = output
            if placeholder.placeholder_format.type == PP_PLACEHOLDER_TYPE.TABLE:
                print(f"Found table placeholder: {placeholder.name} | {placeholder.placeholder_format.type}")
                table_arr = slide_data.get("tables", [])
                if len(table_arr) > 0:
                    table_data = table_arr[tables_index]
                
                    rows = len(table_data["rows"]) + 1 # +1 for header
                    cols = len(table_data["headers"])
                    table = placeholder.insert_table(rows, cols).table
                    # Set header
                    for col_index, header in enumerate(table_data["headers"]):
                        table.cell(0, col_index).text = header
                    # Set rows
                    for row_index, row_data in enumerate(table_data["rows"], start=1):
                        for col_index, cell_data in enumerate(row_data):
                            table.cell(row_index, col_index).text = str(cell_data)
                    tables_index += 1

            # Picture placeholder needs to go last as it becomes invalid after insertion    
            elif placeholder.placeholder_format.type == PP_PLACEHOLDER_TYPE.PICTURE:
                print(f"Found picture placeholder: {placeholder.name} | {placeholder.placeholder_format.type}")
                pictures_arr = slide_data.get("pictures", [])
                if len(pictures_arr) > 0:
                    try:
                        picture_url = pictures_arr[images_index]
                        # regular expression to determine if it is a jpg or png
                        file_ext = re.search(r'\.(jpg|jpeg|png|gif|bmp|tiff)', picture_url, re.IGNORECASE)              
                        img_path = f"/code/app/temp/slide_{i}_image_{images_index}.{file_ext.group(1) if file_ext else 'jpg'}"
                        # Download image
                        print(f"Downloading image from URL: {picture_url}")
                        async with httpx.AsyncClient() as client:
                            async with client.stream("GET", picture_url, follow_redirects=True) as response:
                                response.raise_for_status()  # Raise error for HTTP failures
                                with open(img_path, "wb") as file:
                                    async for chunk in response.aiter_bytes(1024):
                                        file.write(chunk)
                                # Insert picture
                                if(response.status_code == 200):
                                    picture = placeholder.insert_picture(img_path)
                                    images_index += 1
                                    print(f"Inserted picture from {picture_url} [{img_path}] into slide.")
                    except Exception as e:
                        print(f"Error downloading or inserting image: {e}")

            
    output_name = f'generated_presentation_{int(time.time())}.pptx'
    output_path = f'/code/app/output/{output_name}'
    prs.save(output_path)

    #return FileResponse(output_path, media_type='application/vnd.openxmlformats-officedocument.presentationml.presentation', filename='generated_presentation.pptx')
    return f"/download?file_path={output_name}" 


@app.get(
    "/download",
    tags=["APIs"],
    response_class=FileResponse,
)
async def download_pptx(file_path: Union[str, None] = Query(default=None, max_length=200)):
    
    
    if file_path is None:
        return {"error": "file_path query parameter is required."}
    modified_file_path = file_path.replace("..", "") if file_path else None
    modified_file_path = f"/code/app/output/{modified_file_path}"
    return FileResponse(modified_file_path, media_type='application/vnd.openxmlformats-officedocument.presentationml.presentation', filename=file_path)


# @app.get(
#     "/generate",
#     tags=["APIs"],
# )
async def generate_pptx_static(request: Request, title: Union[str, None] = Query(default="Hello World", max_length=50), content: Union[str, None] = Query(default="Something at nothing", max_length=50)): 
    data = {
        "template": '/code/app/templates/template.pptx',
        "slides": [
            {
                "title": title 
            },
            {
                "agenda": [
                    "Introduction",
                    "Main Topic",
                    "Conclusion"
                ]
            },
            {
                "title": "Introduction - Powerpoint Generation with GenAI",
                "pictures": [
                    "https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/media/managed-virtual-network/diagram-managed-network.png?view=foundry-classic"
                ]
            },
            {
                "sectionname": "Main Topic",
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
                "content": content,
                "tables": [
                    { 
                        "headers": ["Year", "Earnings", "Profit"],
                        "rows": [
                            ["2023", 30000000, 5000000],
                            ["2024", 25000000, 4000000],
                            ["2025", 35000000, 6000000]
                        ]
                    }
                ]
            },
            {
                "thanks": "Thank you for your attention!",
                "contactinfo": "GenAI PPTX Bot\n- contact@nothing.com\n- 555-123-4567"
            }
        ]
    }
    return await generate_pptx(data)

@app.post(
    "/generate",
    tags=["APIs"],
    description="Generate a PPTX presentation based on the provided JSON structure."
)
async def generate_pptx_dynamic(request: Request, body: dict = Body(...)): 
    downloadpath = await generate_pptx(body)
    return { "download_url": f"{request.url.scheme}://{request.url.hostname}:{request.url.port if request.url.port else '443'}{downloadpath}" }