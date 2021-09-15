from django.shortcuts import render


# Create your views here.
def calc(request, first_number, action, second_number):
    if action == '+':
        result = first_number + second_number
    elif action == '-':
        result = first_number - second_number
    elif action == '*':
        result = first_number * second_number
    elif action == ':':
        if second_number == 0:
            return render(request, 'calc.html', {'result': 'Cannot divide by zero '})

        result = first_number / second_number
    else:
        result = 'enter one of this operators - "+" , "-", ":", "*"'
        return render(request, 'calc.html', {'result': result})

    return render(request, 'calc.html',
                  {'first_number': first_number, 'second_number': second_number, 'result': f'= {result}',
                   'new_action': action})
