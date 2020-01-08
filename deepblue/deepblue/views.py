from django.db import connection
from django.http import HttpResponse
import random 

def deepblue(request):
    #   with connection.cursor() as cursor:
    totalperson=random.randint(40,50)
    person_for_reg=random.randint(30,35)
    person_for_opd=totalperson-person_for_reg
    # for i in range(0,50):
    #     print(" person_for_reg  "+ str(person_for_reg)+"  person_for_opd  "+ str(person_for_opd))
        
    # sql=""
    # print(" person_for_reg  "+ str(person_for_reg)+"  person_for_opd  "+ str(person_for_opd))
    # print("hello")
    time=8.00
    minutes=0.00
    no_of_waiting_queue=[]
    no_of_waiting_queue.append(0)
    arriving_time=[]
    arriving_time.append(time)
    service_time=time
    step_in=[]
    step_in.append(time)
    step_out=[]
    waiting_duration=[]
    created_queue_hours=[]
    created_queue_hours.append(int(time))
    # print(arriving_time)
    arrival_rate=[]
    arrival_rate1=[]
    service_rate=[]
    service_rate1=[]
    a=8.00
    # step_out.append(8.08)
    time_interval=[]
    table=[]
    table.append(["arriving_time","step_in","step_out","waiting_duration","created_queue_hours","no_of_waiting_queue","arrival_rate","service_rate"])
    total=0
    for i in range(0,1500):
        if(time>=8.00 and time<=18.00):
            minutes=round(random.uniform(0.15,0.30), 2)
            # print(i)
            # print(minutes)
            service_time=round(random.uniform(0.25,0.30), 2)
            if(round((step_in[i]+service_time)-float(int((step_in[i]+service_time))),2)>=0.60):
                step_out.append(round((step_in[i]+service_time+0.40),2))
            else:
                step_out.append(round((step_in[i]+service_time),2))
            time=round((time+minutes),2)
            # print(round(time-float(int(time)),2))
            if(round(time-float(int(time)),2)>=0.6):
                time=time+0.40
            # print(time)
            total=i
            arriving_time.append(round(time,2))
            if(arriving_time[i+1]>step_out[i]):
                step_in.append(arriving_time[i+1])
            else:
                step_in.append(step_out[i])

            created_queue_hours.append(int(time))
            if((int(step_out[i])-int(arriving_time[i]))==1):
                if(round((step_out[i]-arriving_time[i]-0.40))>=0.60):
                    waiting_duration.append(round((step_out[i]-arriving_time[i]),2))
                else:
                    waiting_duration.append(round((step_out[i]-arriving_time[i]-0.40),2))
            elif((int(step_out[i])-int(arriving_time[i]))==2):
                if(round((step_out[i]-arriving_time[i]-0.80),2)<1.2):
                    waiting_duration.append(round((step_out[i]-arriving_time[i]-0.40),2))
                else:
                    waiting_duration.append(round((step_out[i]-arriving_time[i]),2))
            elif((int(step_out[i])-int(arriving_time[i]))==3):
                if(round((step_out[i]-arriving_time[i]-1.2),2)<1.8):
                    waiting_duration.append(round((step_out[i]-arriving_time[i]-0.40),2))
                else:
                    waiting_duration.append(round((step_out[i]-arriving_time[i]),2))
            elif((int(step_out[i])-int(arriving_time[i]))==4):
                if(round((step_out[i]-arriving_time[i]-1.6),2)<2.4):
                    waiting_duration.append(round((step_out[i]-arriving_time[i]-0.40),2))
                else:
                    waiting_duration.append(round((step_out[i]-arriving_time[i]),2))
            elif((int(step_out[i])-int(arriving_time[i]))==5):
                if(round((step_out[i]-arriving_time[i]-2.0),2)<3.0):
                    waiting_duration.append(round((step_out[i]-arriving_time[i]-0.40),2))
                else:
                    waiting_duration.append(round((step_out[i]-arriving_time[i]),2))
            else:
                    waiting_duration.append(round((step_out[i]-arriving_time[i]),2))
        else:
            if(i>=len(arriving_time)):
                    break
            minutes=round(random.uniform(0.20,0.30), 2)
            # print(i)
            # print(minutes)
            service_time=round(random.uniform(0.20,0.25), 2)
            if((step_in[i]+service_time)-float(int((step_in[i]+service_time)))>=0.60):
                step_out.append(round((step_in[i]+service_time+0.40),2))
            if((step_in[i]+service_time)-float(int((step_in[i]+service_time)))<0.60):
                step_out.append(round((step_in[i]+service_time),2))
            step_in.append(step_out[i])
            time=round((time+minutes),2)
            # print(round(time-float(int(time)),2))
            if(round(time-float(int(time)),2)>=0.6):
                time=time+0.40
                
            # print(time)
            total=i
            # arriving_time.append(round(time,2))
            created_queue_hours.append(int(time))
            if((int(step_out[i])-int(arriving_time[i]))==1):
                if(round((step_out[i]-arriving_time[i]-0.40))>=0.60):
                    waiting_duration.append(round((step_out[i]-arriving_time[i]),2))
                else:
                    waiting_duration.append(round((step_out[i]-arriving_time[i]-0.40),2))
            elif((int(step_out[i])-int(arriving_time[i]))==2):
                if(round((step_out[i]-arriving_time[i]-0.80),2)<1.2):
                    waiting_duration.append(round((step_out[i]-arriving_time[i]-0.40),2))
                else:
                    waiting_duration.append(round((step_out[i]-arriving_time[i]),2))
            elif((int(step_out[i])-int(arriving_time[i]))==3):
                if(round((step_out[i]-arriving_time[i]-1.2),2)<1.8):
                    waiting_duration.append(round((step_out[i]-arriving_time[i]-0.40),2))
                else:
                    waiting_duration.append(round((step_out[i]-arriving_time[i]),2))
            elif((int(step_out[i])-int(arriving_time[i]))==4):
                if(round((step_out[i]-arriving_time[i]-1.6),2)<2.4):
                    waiting_duration.append(round((step_out[i]-arriving_time[i]-0.40),2))
                else:
                    waiting_duration.append(round((step_out[i]-arriving_time[i]),2))
            elif((int(step_out[i])-int(arriving_time[i]))==5):
                if(round((step_out[i]-arriving_time[i]-2.0),2)<3.0):
                    waiting_duration.append(round((step_out[i]-arriving_time[i]-0.40),2))
                else:
                    waiting_duration.append(round((step_out[i]-arriving_time[i]),2))
            else:
                    waiting_duration.append(round((step_out[i]-arriving_time[i]),2))
            

    for j in range(1,len(arriving_time)):
        count=1
        for k in range(0,j):
            if(arriving_time[j]<=step_in[k]):
                count+=1
        no_of_waiting_queue.append(count)
    for i in range(0,100):
        time_interval.append(a)
        a=round((a+0.10),2)
        if(round(a-float(int(a)),2)>=0.6):
            a=a+0.40
    for i in range(0,99):
        count=0
        counter=0
        for j in range(0,len(arriving_time)):
            if(arriving_time[j]>=time_interval[i] and arriving_time[j]<(time_interval[i+1])):
                count+=1
            if(step_in[j]>=time_interval[i] and step_in[j]<(time_interval[i+1])):
                counter+=1
        service_rate.append(counter)
        arrival_rate.append(count)
        # print("time_interval  "+str(time_interval[i])+" "+str(count)+" "+str(counter))
    for j in range(0,len(arriving_time)):
        for i in range(0,99):
            if(arriving_time[j]>=time_interval[i] and arriving_time[j]<(time_interval[i+1])):
                # print("arrival  "+str(time_interval[i])+"      "+str(time_interval[i+1])+"    "+str(arriving_time[j])+"    "+str(arrival_rate[i])+"   "+str(i)+"   "+str(j))
                arrival_rate1.append(str(arrival_rate[i]))
            
            if(step_in[j]>=time_interval[i] and step_in[j]<(time_interval[i+1])):
                # print("service    "+str(time_interval[i])+"      "+str(time_interval[i+1])+"    "+str(step_in[j])+"     "+str(service_rate[i]))
                service_rate1.append(str(service_rate[i]))
            # if(i==98):
            #     arrival_rate1.append(0)
            # if(i==98):
            #     service_rate1.append(0)
        
        
    for i in range(0,len(arrival_rate1)):
        # table.append(["created_queue_hours","waiting_duration","no_of_waiting_queue","arrival_rate","service_rate"])
        table.append([str(arriving_time[i]),str(step_in[i]),str(step_out[i]),str(waiting_duration[i]),str(created_queue_hours[i]),str(no_of_waiting_queue[i]),str(arrival_rate1[i]),str(service_rate1[i])])
    for i in range(0,len(service_rate1)):
        for j in range(0,8):
            print(table[i][j],end=" \t")
        print("\r")
    print(arrival_rate)
    print(service_rate)
    print(arrival_rate1,len(arrival_rate1))
    print(service_rate1,len(service_rate1))
    print(time_interval)
    print("arriving_time"+str(arriving_time)+" "+str(len(arriving_time)))
    print("waiting_duration"+str(waiting_duration)+" "+str(len(waiting_duration)))
    print("step_in"+str(step_in)+" "+str(len(step_in)))
    print("step_out"+str(step_out)+" "+str(len(step_out)))
    print("no_of_waiting_queue"+str(no_of_waiting_queue)+" "+str(len(no_of_waiting_queue)))
    print("created_queue_hours"+str(created_queue_hours)+" "+str(len(created_queue_hours)))
    #below this is a script for storing data in mysql database
    with connection.cursor() as cursor:
        # sql="INSERT INTO `table 1` VALUES ('Number in the queue/DeptNumber', 'Shift (M/A/E)', 'Queue Type (Reg','Created Queue Hours', 'Created Queue Day of Week', 'Waiting Duration', 'Number of Waiting Queue', 'Arrival Rate', 'Service Rate')"
        # cursor.execute(sql)
        
        
        # sql="INSERT INTO `table 1` VALUES {}".format(str(result))
        # cursor.execute(sql)
        # print(sql)
        for i in range(0,len(service_rate1)-1):
            shift=0
            if(created_queue_hours[i]>=8 and created_queue_hours[i]<12):
                #shift 1 =8 to 12 hours
                shift=1
            elif(created_queue_hours[i]>=12 and created_queue_hours[i]<16):
                #shift 2 =12 to 4 hours
                shift=2
            else:
                #shift 2 =4 to 10 hours
                shift=3

            SQL="INSERT INTO `table 1` VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(str(401),str(shift),str("07/01/2020"),str(created_queue_hours[i]),str(waiting_duration[i]),str(no_of_waiting_queue[i]),str(arrival_rate1[i]),str(service_rate1[i]))
            print(SQL)
            cursor.execute(SQL)
    return HttpResponse("Successfull")
           

