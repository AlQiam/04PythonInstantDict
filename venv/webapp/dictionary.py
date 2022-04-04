import justpy as jp
from definition import Definition


class Dictionary:
    path = '/dictionary'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text='Instant English Dictionary', classes='text-4xl m-2')
        jp.Div(a=div, text='Get the definition of any English word instantly as you type',
               classes='text-lg')
        input_div = jp.Div(a=div, classes='grid grid-cols-2')

        input_box = jp.Input(a=input_div, placeholder='Type in a word here', classes='m-2 bg-gray-100 border-2 '
                                                                                     'border-black-500 rounded w-64 '
                                                                                     'focus:outline-none '
                                                                                     'py-2 px-4 focus:bg-white')
        output_div = jp.Div(a=div, classes='m-2 p-2 text-lg border-2 h- bg-gray-100')
        jp.Button(a=input_div, text='Get Definition', click=cls.get_definition, outputdiv=output_div,
                  classes='border- text-black-500 m-2 p-2 bg-gray-300', inputbox=input_box)

        return wp

    @staticmethod
    def get_definition(widget, msg):
        defined = Definition(widget.inputbox.value).get()
        widget.outputdiv.text = '\n'.join(defined) + '\n'
        # A static method is a method inside the class that behaves like a function
