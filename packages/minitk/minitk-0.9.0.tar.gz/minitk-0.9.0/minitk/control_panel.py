import tkinter as tk
from tkinter import ttk
from typing import Optional, Callable, Union, TypeVar
from pynput import keyboard
from PIL import Image, ImageTk
from functools import partial


T = TypeVar("T")



class ControlPanel(tk.Frame):
    
    def __init__(self, title:str='Control', offset:tuple[int, int]=(0,0), exit_callback:Optional[callable]=None):
        """Minimalist control panel for parameter tuning. Update widgets with the update method."""

        master = tk.Tk()
        super().__init__(master)
        master.title(title)
        master.geometry(f"+{offset[0]}+{offset[1]}")
        self.master = master
        self.title = title
        self.grid()
        self.rows:dict[int, int] = {}

        if not exit_callback: exit_callback = self.on_closing
        self.master.protocol("WM_DELETE_WINDOW", exit_callback)
        self.parent = None

        self.widgets = {}
        self.containers = {}
        self.images = {}
        self.combobox_selected_values = {}
        self.combobox_callbacks = {}
        self.radiomenu_mapping = {}


    def __set_widget_position(self, widget:tk.Widget, column:int=0):
        if column not in self.rows:
            self.rows[column] = 0

        sticky = tk.NSEW
        if isinstance(widget, tk.Radiobutton):
            sticky = tk.W

        widget.grid(column=column, row=self.rows[column], sticky=sticky)
        self.rows[column] += 1

        for container in self.containers.values():
            if container['open']:
                container['childs'].append(widget)


    def __add_hotkey(self, key:str, widget:tk.Widget):

        if not hasattr(self, 'hotkeys'):
            self.hotkeys = KeyboardHotkeys()

        self.hotkeys.bindings[key] = [False, widget]


    def update(self) -> None:

        if len(self.widgets) == 0:
            self.master.destroy()
            return

        for name in self.containers:
            if not self.containers[name]['initialized']:
                self.widgets[name].invoke()
                self.widgets[name].invoke()
                self.containers[name]['initialized'] = True
                
        if hasattr(self, 'hotkeys'):
            for _, binding in self.hotkeys.bindings.items():
                if binding[0]:
                    binding[1].invoke()
                    binding[0] = False

        for name, callback in self.combobox_callbacks.items():
            selected_value = self.get_state(name)
            if selected_value != self.combobox_selected_values[name]:
                self.combobox_selected_values[name] = selected_value
                callback(selected_value)

        return super().update()
        

    def create_button(
            self, 
            name:str, 
            callback:Optional[Callable[[],None]] = None, 
            hotkey:str = None, 
            column:int = 0, 
            visible:bool = True,
        ):

        self.widgets[name] = tk.Button(self, command=callback)
        self.widgets[name]["text"] = name

        self.__set_widget_position(self.widgets[name], column)

        if hotkey is not None:
            self.__add_hotkey(hotkey, self.widgets[name])
            self.widgets[name]["text"] = f'{name} ({hotkey})'

        if not visible:
            self.widgets[name].grid_remove()


    def create_check_button(
            self, 
            name:str, 
            default:bool = False, 
            callback:Optional[Callable[[bool],None]] = None, 
            hotkey:str = None, 
            column:int = 0, 
            visible:bool = True,
        ):

        self.widgets[name] = ttk.Checkbutton(self)
        self.widgets[name]["text"] = name
        self.__set_widget_position(self.widgets[name], column)

        self.widgets[name].invoke()
        if not default: 
            self.widgets[name].invoke()

        if callback is not None:
            self.widgets[name]["command"] = lambda: callback(self.get_state(name))

        if hotkey is not None:
            self.__add_hotkey(hotkey, self.widgets[name])
            self.widgets[name]["text"] = f'{name} ({hotkey})'

        if not visible:
            self.widgets[name].grid_remove()


    def create_menu(
            self, 
            name:str, 
            choices:list[T], 
            callback:Optional[Callable[[T],None]] = None, 
            column:int = 0,
        ):

        self.widgets[f'{name}_variable'] = tk.StringVar(self)
        self.widgets[f'{name}_variable'].set(choices[0]) # default value

        self.__set_widget_position(tk.Label(self, text=name), column)

        self.widgets[name] = tk.OptionMenu(self, self.widgets[f'{name}_variable'], *choices, command=callback)

        self.__set_widget_position(self.widgets[name], column)


    def create_scrollmenu(
            self, 
            name:str, 
            choices:list[T], 
            callback:Optional[Callable[[T],None]] = None, 
            column:int = 0,
            editable:bool = False,
        ):

        self.__set_widget_position(tk.Label(self, text=name), column)

        width = max([len(str(choice)) for choice in choices])

        if editable:
            self.widgets[name] = ttk.Combobox(self, textvariable=tk.StringVar(self), width=width)
        else:
            self.widgets[name] = ttk.Combobox(self, textvariable=tk.StringVar(self), width=width, state="readonly")
        self.widgets[name]["values"] = choices
        self.widgets[name].current(0)

        self.combobox_selected_values[name] = choices[0]
        self.combobox_callbacks[name] = callback

        self.__set_widget_position(self.widgets[name], column)


    def create_spinbox(
            self, 
            name:str, 
            start: int = 0,
            end: int = 10,
            default: Optional[int] = None,
            callback:Optional[Callable[[T],None]] = None, 
            column:int = 0,
            editable:bool = True,
        ):

        self.__set_widget_position(tk.Label(self, text=name), column)

        choices = list(range(start, end + 1))

        width = max([len(str(choice)) for choice in choices])

        if editable:
            self.widgets[name] = ttk.Spinbox(self, textvariable=tk.StringVar(self), width=width)
        else:
            self.widgets[name] = ttk.Spinbox(self, textvariable=tk.StringVar(self), width=width, state="readonly")
        self.widgets[name]["values"] = choices

        self.combobox_selected_values[name] = choices[0]
        self.combobox_callbacks[name] = callback

        default = start if default is None else default
        self.set_state(name, default)

        self.__set_widget_position(self.widgets[name], column)

    
    def create_slider(
            self, 
            name:str, 
            start:float = 0.0, 
            end:float = 1.0, 
            step:float = 0.01, 
            default:Optional[float] = None, 
            show_value:bool = True, 
            callback:Optional[Callable[[float],None]] = None, 
            column:int = 0, 
        ):
        
        self.widgets[name] = tk.Scale(self, label=name, from_=start, to=end, resolution=step, orient=tk.HORIZONTAL, showvalue=show_value, command=callback)

        default = start if default is None else default
        self.widgets[name].set(default)

        self.__set_widget_position(self.widgets[name], column)


    def create_radiomenu(
            self, 
            name:str, 
            choices:list[T], 
            default: Optional[T] = None,
            callback:Optional[Callable[[T],None]] = None, 
            column:int = 0,
        ):

        self.widgets[f"{name}_variable"] = tk.IntVar()
        self.radiomenu_mapping[name] = {}

        self.__set_widget_position(tk.Label(self, text=name), column)

        for index, choice in enumerate(choices):
            self.widgets[f"{name}_{index}"] = tk.Radiobutton(self, text=choice, value=index, variable=self.widgets[f"{name}_variable"], command=partial(callback, choice))
            self.__set_widget_position(self.widgets[f"{name}_{index}"], column)
            self.radiomenu_mapping[name][index] = choice

        if default is not None:
            self.set_state(name, default)
        else:
            self.set_state(name, choices[0])


    def start_container(self, name:str, default:bool=False):
        self.create_check_button(name, default)
        self.containers[name] = {'open': True, 'childs': [], 'default': default, 'initialized': False}


    def end_container(self, name:str):
        self.containers[name]['open'] = False

        def toggle(state):
            for child in self.containers[name]['childs']:
                if state: child.grid()
                else: child.grid_remove()
        
        self.widgets[name]['command'] = lambda: toggle(self.get_state(name))


    def add_separator(self):
        separator = ttk.Separator(self, orient='horizontal')
        self.__set_widget_position(separator)


    def get_state(self, name:str):

        if name in self.radiomenu_mapping:
            index = self.widgets[f"{name}_variable"].get()
            return self.radiomenu_mapping[name][index]

        try:
            widget = self.widgets[name]
        except KeyError:
            raise KeyError(f"The widget with name '{name}' does not exist.")

        if isinstance(widget, ttk.Checkbutton):
            return widget.instate(['selected'])

        elif isinstance(widget, tk.OptionMenu):
            return self.widgets[f'{name}_variable'].get()

        elif isinstance(widget, tk.Scale):
            return widget.get()
        
        elif isinstance(widget, ttk.Combobox):
            return widget.get()
        
        elif isinstance(widget, ttk.Spinbox):
            return widget.get()
                    
        raise NotImplementedError


    def set_state(self, name:str, state):

        if name in self.radiomenu_mapping:
            index = list(self.radiomenu_mapping[name].values()).index(state)
            self.widgets[f"{name}_{index}"].invoke()
            return

        try:
            widget = self.widgets[name]
        except KeyError:
            raise KeyError(f"The widget with name '{name}' does not exist.")

        if isinstance(widget, ttk.Checkbutton):
            if self.get_state(name) != state:
                widget.invoke()

        elif isinstance(widget, tk.OptionMenu):
            self.widgets[f'{name}_variable'].set(state)

        elif isinstance(widget, tk.Scale):
            widget.set(state)

        elif isinstance(widget, ttk.Combobox):
            widget.set(state)

        elif isinstance(widget, ttk.Spinbox):
            widget.set(state)

        else:
            raise NotImplementedError


    def draw_image(self, name:str, image, column:int=0):
        image_pil = Image.fromarray(image, mode="RGB")
        image_tk = ImageTk.PhotoImage(image_pil)
        if name not in self.images:
            dummy_label = tk.Label(self, image=image_tk)
            self.__set_widget_position(dummy_label, column)
            self.images[name] = dummy_label
        self.images[name].configure(image=image_tk)
        self.images[name].image = image_tk


    def attach(self, other:'ControlPanel'):
        other.parent = self
        other.hide()

        def toggle(state):
            if state: other.unhide()
            else: other.hide()

        self.create_check_button(other.title)
        self.widgets[other.title]['command'] = lambda: toggle(self.get_state(other.title))


    def hide(self):
        self.master.withdraw()

    def unhide(self):
        self.master.deiconify()

    def on_closing(self):
        if self.parent:
            self.parent.widgets[self.title].state(['!selected'])
        self.hide()


class KeyboardHotkeys:

    def __init__(self):

        self.bindings = {}

        self.keyboard_listener = keyboard.Listener(on_press=self.__on_key_press)
        self.keyboard_listener.start()

    def __on_key_press(self, key:Union[keyboard.KeyCode, keyboard.Key]):
        
        if isinstance(key, keyboard.KeyCode):
            if key.char in self.bindings:
                self.bindings[key.char][0] = True

        elif isinstance(key, keyboard.Key):
            if key.name in self.bindings:
                self.bindings[key.name][0] = True
                