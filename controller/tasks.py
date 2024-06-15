import os
from dotenv import load_dotenv

from src.tools import get_image

load_dotenv()

from src.agent.constants import PREDEFINED_CLASS

def get_image_captioning(vsion_model, image): 
    object_detection = f"""Detect everything you see in the provided picture. Tell me what you can see in the image. In addition, you should focus on these things: 
   {PREDEFINED_CLASS}
   You should tell the number of each object that you can define and list them in bullet points.
"""
    caption_pipeline = vsion_model.chat(prompt=object_detection, 
                                  image=image)
    return caption_pipeline

def analyze_image_information(langauge_model, image_description):
    prompt = f"""
    Analyze the following image information and provide insights based on the criteria given below:

    Image Description:
    {image_description}

    Criteria:
    1. Brand Logos: Identify any brand logos mentioned in the description or OCR results.
    2. Products: Mention any products such as beer kegs and bottles.
    3. Customers: Describe the number of customers, their activities, and emotions.
    4. Promotional Materials: Identify any posters, banners, and billboards.
    5. Setup Context: Determine the scene context (e.g., bar, restaurant, grocery store, or supermarket).

    Insights:
    """
    chat_completion = langauge_model.chat(prompt)
    return chat_completion

def pipeline(language_model, vision_model, image): 
    image = get_image(image)
    image_captioning = get_image_captioning(vision_model=vision_model, 
                                            image=image)
    analytic_result = analyze_image_information(langauge_model=language_model, 
                                                image_description=image_captioning)
    return analytic_result