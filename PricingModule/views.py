from datetime import timedelta
from django.shortcuts import render

from myapp.models import PricingConfig


def getBillFormTemplate(request):
    return render(request, 'bill-form.html', {})
    
def getFinalBill(request):
    # getting data from request
    distance = int(request.GET.get('distance'))
    time = int(request.GET.get('time'))
    print(distance,time)
    # checking if request contain mandatory fields    
    if not time or not distance:        
        return render(request, 'bill-form.html', {'showDistanceErr':True, 'showTimeErr':True})
    
    # finding data from database
    # if we have multiple enable config for this i am finding the highest-distance-limit
    configs = PricingConfig.objects.filter(
            enable=True,
            distance_limit__gte=distance,
            time_limit__gte=time,
        ).order_by('-distance_limit')
    print(configs.exists())
    
    if configs.exists():
            config = configs.first()
            dbp = config.distance_base_price
            dap = config.distance_additional_price
            tmf = config.time_multiplier_factor
            price = (dbp + (distance * dap)) * tmf
            data={'dataAvailable':True,'price': price,
                'distanceBasePrice':dbp,
                'distanceAdditionalPrice':dap,
                'timeMultiplierFactor':tmf
                }
            return render(request,'final-bill.html',data)
        
        # If no matching configuration is found, return an error response
    elif PricingConfig.objects.filter(enable=True).exists():
        data={'noMatchingFound':True}
        return render(request,'final-bill.html',data)
    else:
        return render(request,'final-bill.html',{})
