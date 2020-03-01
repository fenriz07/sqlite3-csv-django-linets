import csv
import collections
from django.views import View
from Export.models import Products
from django.http import HttpResponse
from django.views.generic.detail import SingleObjectMixin

class ExportAPIView(SingleObjectMixin,View):

    def get(self,request):

        productsGroup = Products.objects.all().order_by('model');
        
        grouped = collections.defaultdict(list)

        for item in  productsGroup:
            grouped[item.model].append(item)

        collectProducts = {}

        for model, group in grouped.items():

            collectProducts[model] = []

            for product in group:

                collectProducts[model].append( [product.name,product.sku,product.attribute_color] )

        rowsCsv = []

        formato = "|sku=%s,color=%s"
        
        for model in collectProducts:
           name = ''
           configurations_variantions = ''

           for product in collectProducts[model]:
               name = product[0]
               configurations_variantions += "|sku=%s,color=%s" % ( product[1],product[2])

           rowsCsv.append( [ model,name,configurations_variantions[1:]] )
   

        return self.responseCsv(rowsCsv)

    def responseCsv(self,rows):

           response = HttpResponse(content_type='text/csv')
           response['Content-Disposition'] = 'attachment; filename="products.csv"'

           writer = csv.writer(response)

           writer.writerow(['sku(model)', 'name', 'configurations_variantions'])

           for row in rows:
               writer.writerow( row )
           
           return response