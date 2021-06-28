from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "90f88c6b30msh6878bf751006f7ap146ef6jsnde0275613b83",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()


# Create your views here.
def covid_data_view(request):
	country_list=[]
	total_results=int(response['results'])

	for x in range(0,total_results):

		country_list.append(response['response'][x]['country'])
	if request.method=="POST":
		selectedcountry=request.POST['selectedcountry']
		
		for x in range(0,total_results):
			if selectedcountry==response['response'][x]['country']:
				new=response['response'][x]['cases']['new']
				active=response['response'][x]['cases']['active']
				critical=response['response'][x]['cases']['critical']
				recovered=response['response'][x]['cases']['recovered']
				total=response['response'][x]['cases']['total']
				deaths=int(total)-int(active)-int(recovered)

		context={'selectedcountry':selectedcountry,'country_list':country_list,'new':new,'active':active,'critical':critical,'recovered':recovered,'deaths':deaths,'total':total}
		return render(request,'covid.html',context)
				
	context={'country_list':country_list}
	return render(request,'covid.html',context)