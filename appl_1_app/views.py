import datetime,math
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Count, Avg, Min, Max, StdDev, Sum
from .forms import Form_x, Model_form_X
from .models import Model_X
from django.db.models import Field




def form_1(request):
    form_1 = Form_x()
    print(form_1)
    return render(request, "form_1.html", {"form_1": form_1})

def get(request):
    if request.method == "GET":
        form = Form_x(request.GET)
        if form.is_valid():
            task_value = form.cleaned_data["task"]
            x_value = form.cleaned_data["x"]

            get_obj = Model_X(task=task_value, x=x_value)
            get_obj.save()

            return redirect("appl_1_app:result")
    else:
        form = Form_x()

    return render(request, "form_1.html", {"form": form})



def form_2(request):
    print("request.method: ", request.method)
    if request.method == "POST":
        form = Model_form_X(request.POST)
        if form.is_valid():
            print("\nform_is_valid:\n", form)
            form.save()
            return redirect("appl_1_app:result")
    else:
        form = Model_form_X()
        print("\nform_else:\n", form)
    context = {"form": form}
    print("\ncontext:\n", context)
    return render(request, "form_2.html", context)


def form_3(request):
    print("request.method: ", request.method)
    if request.method == "POST":
        form = Model_form_X(request.POST)
        if form.is_valid():
            print("\nform_is_valid:\n", form)
            form.save()
            return redirect("appl_1_app:result")
    else:
        form = Model_form_X()
        print("\nform_else:\n", form)
    context = {"form": form}
    print("\ncontext:\n", context)
    return render(request, "form_3.html", context)

    

def task(x_value): 
    result = ''
    if x_value > 0:
        result = 'число больше нуля'
    elif x_value < 0:
        result = 'число меньше нуля'
    else:
        result = 'число равно нулю'
    
    return result



def result(request):
    object_list = Model_X.objects.all().order_by("-id")
    print("\n\nobject_list: ", object_list)

    task_formulation = object_list.values("task")[0]["task"]
    task_id = object_list.values("id")[0]["id"]
    print("task_id task_formulation: ", task_id, task_formulation)


    values_list = object_list.values_list()[0]
    print("\nvalues_list: ", values_list)
    last_values = [values_list[1], values_list[2]]
    print("\nlast_values:", last_values)


    result = task(last_values[1])
    print("\nresult: ", result)
  
    
    
    update_obj = Model_X.objects.filter(id=task_id)
    update_result = result
    update_obj.update(result = update_result)

    context = {
        "task_formulation": task_formulation,
        "last_values": last_values,
        "result": result,
    }
    return render(request, "result.html", context)


def table(request):
    objects_values = Model_X.objects.values()
    print("\nobjects_values:", objects_values)
    objects_values_list = (
        Model_X.objects.values_list().filter(id__gte=8).order_by("-x")
    )  
    print("\nobjects_values_list:", objects_values_list)
    cur_objects = objects_values_list
    statics_val = [
        cur_objects.aggregate(Avg("x")),
    ]
    print("\nstatics_val:", statics_val)
    statics = {"statics_val": statics_val}
    
    fields = Model_X._meta.get_fields()
    print("\nfields", fields)
    verbose_name_list = []
    name_list = []
    for e in fields:
        if isinstance(e, Field):
            verbose_name_list.append(e.verbose_name)
            name_list.append(e.name)
    print("\nverbose_name_list:", verbose_name_list)
    print("\nname_list", name_list)
    field_names = verbose_name_list
    context = {
        "objects_values": objects_values,
        "name_list": name_list,
        "objects_values_list": objects_values_list,
        "verbose_name_list": verbose_name_list,
        "statics": statics,
        "field_names": field_names,
    }
    return render(request, "table.html", context)
