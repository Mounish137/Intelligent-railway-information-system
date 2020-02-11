from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

def findtrains(request):
    if request.method == 'POST':
        src = request.POST.get('src')
        dest = request.POST.get('dest')
        cur = connection.cursor()
        cur.execute('use railwaymodel;')
        cur.execute(
        '''select r4.* from
        (select r1.trainno from
        (select trainno,distance from trainstops where stid='%s') as r1
        inner join
        (select trainno,distance from trainstops where stid='%s') as r2
           on R1.trainno = R2.trainno where r1.distance < r2.distance) as r3
           inner JOIN
           train as r4
           on r3.trainno = r4.trainno;'''%(src,dest))
        res = cur.fetchall()
        context = {'trains_result':res}
        return HttpResponse(render(request,'findtrains.html',context))
        cur.close()
    else:
        return HttpResponse(render(request,'findtrains.html'))
