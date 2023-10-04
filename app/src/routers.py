# -*- coding: utf-8 -*-
from fastapi import APIRouter, Response, Depends, HTTPException, Request, File, UploadFile, Form
from sqlalchemy.orm import Session
from PIL import Image
import base64
from io import BytesIO
import os



router = APIRouter()

#Actualizar un usuario por  ID
@router.post('/get_card')
async def get_card(
    request: Request, 
    response:Response,
    image: UploadFile = File(...)):

    buffered = BytesIO()
    image = Image.open(BytesIO(image.file.read()))

    width, height = image.size
    new_size = (width//2, height//2)
    resized_image = image.resize(new_size)
    
    resized_image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())

    return {
        "name": img_str
    }