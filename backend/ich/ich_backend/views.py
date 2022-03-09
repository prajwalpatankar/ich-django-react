from .serializers import *
from .models import *
from rest_framework import viewsets
# import requests
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


# import torch 
# import torchvision.transforms as T
# import torchvision.models as models
# from torchvision.utils import make_grid
# from PIL import Image

# class ImageCreateAPIView(viewsets.ModelViewSet):
# 	serializer_class = imageSerializer
# 	queryset = MyImage.objects.all()


class UploadDicomViewset(viewsets.ModelViewSet):
	serializer_class = dicomSerializer
	queryset = DicomFile.objects.all()





# @api_view(('GET',))
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
# def model_call(request):
# 	req_id = request.GET.get('id')
# 	img_obj = MyImage.objects.get(id=req_id)
# 	django_img = img_obj.model_pic
# 	img = Image.open(django_img)

	# model_path = "ich_backend/mod.pth"	
	# device = 'cpu'
	# classes = ['detected', 'not_detected']

	# model = torch.load(model_path, map_location=torch.device(device) )
	# for parameter in model.parameters():
	# 	parameter.requires_grad = False

	# model.eval()
	# # print(model)
		
	# test_transforms = T.Compose([
	# 	T.Resize(256),
	# 	T.ToTensor()
	# ])

	# # img = Image.open(image_path)
	# image_tensor = test_transforms(img).float()
	# image_tensor = image_tensor.unsqueeze_(0)
	# # input = Variable(image_tensor)
	# input = image_tensor.to(device)
	# output = model(input)
	# if device == 'cpu':
	# 	index = output.data.cpu().numpy().argmax()
	# else:
	# 	index = output.data.cuda().numpy().argmax()


	# print("ANSWER : ",classes[index],"[", index,"]" )
	# return Response(data)