import wx
import wx.lib.scrolledpanel as scrolled
import image
from tkinter import *
from tkinter import messagebox


class MainFrame(wx.Frame):

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(MainFrame, self).__init__(*args, style=wx.CAPTION ^ wx.RESIZE_BORDER)
        self.image = image.Image(self, 50, 50, 5, 'Von Neumann', 'non-periodical')
        self.is_animation_running = False
        self.SetSize(size=(300, 440))

        # create a panel in the frame
        self.panel = scrolled.ScrolledPanel(self, -1, size=(300, 400))

        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.AddMany([((10, 10), 0)])

        # Width input
        label_width = wx.StaticText(self.panel, -1, "Width")
        self.input_width = wx.TextCtrl(self.panel, -1, "50", size=(45, -1))

        # Height input
        label_height = wx.StaticText(self.panel, wx.ID_ANY, u"Height")
        self.input_height = wx.TextCtrl(self.panel, -1, "50", size=(45, -1))

        # Box size
        label_box_size = wx.StaticText(self.panel, -1, "Box size")
        self.input_box_size = wx.TextCtrl(self.panel, -1, "5", size=(45, -1))

        hbox_size = wx.BoxSizer(wx.HORIZONTAL)
        hbox_size.AddMany([((2, 2), 0), (label_width, 0), ((2, 2), 0)])
        hbox_size.AddMany([((2, 2), 0), (self.input_width, 0), ((2, 2), 0)])
        hbox_size.AddMany([((2, 2), 0), (label_height, 0), ((2, 2), 0)])
        hbox_size.AddMany([((2, 2), 0), (self.input_height, 0), ((2, 2), 0)])
        hbox_size.AddMany([((2, 2), 0), (label_box_size, 0), ((2, 2), 0)])
        hbox_size.AddMany([((2, 2), 0), (self.input_box_size, 0), ((2, 2), 0)])
        self.vbox.AddMany([((2, 2), 0), (hbox_size, 0), ((2, 2), 0)])

        # Change size button
        self.btn_set_size = wx.Button(self.panel, -1, "Update (and clean) grid")
        self.btn_set_size.Bind(wx.EVT_BUTTON, self.on_set_size_clicked)
        self.vbox.Add(self.btn_set_size, 0, wx.CENTER | wx.EXPAND)
        self.vbox.AddMany([((10, 10), 0)])

        # Neighbourhood
        label_neighbourhood = wx.StaticText(self.panel, -1, "Neighbourhood type ")

        neighbourhood = ['Von Neumann', 'Moore', 'Hexagonal left', 'Hexagonal right', 'Hexagonal random',
                         'Pentagonal random']
        self.combo = wx.ComboBox(self.panel, choices=neighbourhood)
        self.combo.Bind(wx.EVT_COMBOBOX, self.on_neighbourhood_selected)
        self.combo.SetValue('Von Neumann')

        hbox_neighbourhood = wx.BoxSizer(wx.HORIZONTAL)
        hbox_neighbourhood.AddMany([((5, 5), 0), (label_neighbourhood, 0), ((5, 5), 0)])
        hbox_neighbourhood.AddMany([((5, 5), 0), (self.combo, 0), ((5, 5), 0)])
        self.vbox.AddMany([((5, 5), 0), (hbox_neighbourhood, 0), ((5, 5), 0)])

        # Boundary conditions
        label_conditions = wx.StaticText(self.panel, -1, "Boundary conditions ")

        conditions = ['periodical', 'non-periodical']
        self.combo_conditions = wx.ComboBox(self.panel, choices=conditions)
        self.combo_conditions.Bind(wx.EVT_COMBOBOX, self.on_conditions_selected)
        self.combo_conditions.SetValue('non-periodical')

        hbox_conditions = wx.BoxSizer(wx.HORIZONTAL)
        hbox_conditions.AddMany([((5, 5), 0), (label_conditions, 0), ((5, 5), 0)])
        hbox_conditions.AddMany([((6, 5), 0), (self.combo_conditions, 0), ((5, 5), 0)])
        self.vbox.AddMany([((5, 5), 0), (hbox_conditions, 0), ((5, 5), 0)])

        self.vbox.AddMany([((10, 10), 0)])

        # Add seeds
        label_number_of_seeds = wx.StaticText(self.panel, -1, "Number of seeds to add")
        self.input_number_of_seeds = wx.TextCtrl(self.panel, -1, "10", size=(45, -1))
        label_r = wx.StaticText(self.panel, -1, "R")
        self.input_radius = wx.TextCtrl(self.panel, -1, "10", size=(45, -1))

        hbox_size = wx.BoxSizer(wx.HORIZONTAL)
        hbox_size.AddMany([((2, 2), 0), (label_number_of_seeds, 0), ((2, 2), 0)])
        hbox_size.AddMany([((2, 2), 0), (self.input_number_of_seeds, 0), ((2, 2), 0)])
        hbox_size.AddMany([((10, 2), 0), (label_r, 0), ((2, 2), 0)])
        hbox_size.AddMany([((2, 2), 0), (self.input_radius, 0), ((2, 2), 0)])
        self.vbox.AddMany([((2, 2), 0), (hbox_size, 0), ((2, 2), 0)])

        self.vbox.AddMany([((10, 10), 0)])

        # Add randomly
        self.btn_add_randomly = wx.Button(self.panel, -1, "Add randomly")
        self.btn_add_randomly.Bind(wx.EVT_BUTTON, self.on_add_randomly_clicked)
        # Add evenly
        self.btn_add_evenly = wx.Button(self.panel, -1, "Add evenly")
        self.btn_add_evenly.Bind(wx.EVT_BUTTON, self.on_add_evenly_clicked)
        # Add randomly with radius
        self.btn_add_radius = wx.Button(self.panel, -1, "Add with R")
        self.btn_add_radius.Bind(wx.EVT_BUTTON, self.on_add_radius_clicked)

        hbox_seeds_buttons = wx.BoxSizer(wx.HORIZONTAL)
        hbox_seeds_buttons.Add(self.btn_add_randomly)
        hbox_seeds_buttons.Add(self.btn_add_evenly)
        hbox_seeds_buttons.Add(self.btn_add_radius)
        self.vbox.Add(hbox_seeds_buttons, 0, wx.CENTER)

        self.vbox.AddMany([((10, 10), 0)])

        self.st = wx.StaticLine(self.panel, wx.ID_ANY, style=wx.LI_HORIZONTAL)
        self.vbox.Add(self.st, 0, wx.ALL | wx.EXPAND, 5)

        # Buttons
        # Play
        self.btn_play = wx.Button(self.panel, -1, "Play")  # ▶
        font = wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.btn_play.SetFont(font)
        self.btn_play.Bind(wx.EVT_BUTTON, self.on_play_clicked)
        self.vbox.Add(self.btn_play, 0, wx.CENTER)

        # Pause
        self.btn_pause = wx.Button(self.panel, -1, "Pause")  # ❚❚
        self.btn_pause.Bind(wx.EVT_BUTTON, self.on_pause_clicked)
        self.vbox.Add(self.btn_pause, 0, wx.CENTER)

        # Reset
        self.btn_reset = wx.Button(self.panel, -1, "Reset")
        self.btn_reset.Bind(wx.EVT_BUTTON, self.on_reset_clicked)
        self.vbox.Add(self.btn_reset, 0, wx.CENTER)

        # Clean
        self.btn_clean = wx.Button(self.panel, -1, "Clean")
        self.btn_clean.Bind(wx.EVT_BUTTON, self.on_clean_clicked)
        self.vbox.Add(self.btn_clean, 0, wx.CENTER)

        # Animation step time
        self.st = wx.StaticLine(self.panel, wx.ID_ANY, style=wx.LI_HORIZONTAL)
        self.vbox.Add(self.st, 0, wx.ALL | wx.EXPAND, 5)
        hbox_time = wx.BoxSizer(wx.HORIZONTAL)
        label_time = wx.StaticText(self.panel, -1, "Time step")
        conditions = ['0.1 sec', '0.2 sec', '0.3 sec', '0.4 sec',
                      '0.5 sec', '0.6 sec', '0.7 sec', '0.8 sec',
                      '0.9 sec', '1.0 sec']
        self.combo_time = wx.ComboBox(self.panel, choices=conditions)
        self.combo_time.Bind(wx.EVT_COMBOBOX, self.on_time_step_clicked)
        self.combo_time.SetValue('1.0 sec')

        hbox_time.Add(label_time, 0, wx.CENTER)
        hbox_time.Add(self.combo_time, 0, wx.CENTER)
        self.vbox.Add(hbox_time, 0, wx.CENTER)

        self.panel.SetSizer(self.vbox)
        self.CreateStatusBar()
        self.SetStatusText("Welcome!")

        self.Centre()
        self.Show()
        self.Fit()
        self.image.start()

    def handle_add_seeds_error(self, input_text):
        value = None
        try:
            value = int(input_text)
        except ValueError:
            Tk().wm_withdraw()
            messagebox.showerror('Error', 'Illegal characters! Only integers allowed.')
        if value <= 0:
            Tk().wm_withdraw()
            messagebox.showerror('Error', 'Number must be positive.')
        elif value >= self.image.WIDTH * self.image.HEIGHT/2:
            Tk().wm_withdraw()
            messagebox.showerror('Error', 'Number too big.')
            value = self.image.WIDTH * self.image.HEIGHT/2
        return value

    def on_add_evenly_clicked(self, event):
        value = self.handle_add_seeds_error(self.input_number_of_seeds.GetValue())
        if value is not None:
            self.image.add_seeds_evenly(value)

    def on_add_radius_clicked(self, event):
        value = self.handle_add_seeds_error(self.input_number_of_seeds.GetValue())
        r = self.handle_add_seeds_error(self.input_radius.GetValue())
        if value is not None:
            added = self.image.add_seeds_radius(value, r)
            Tk().wm_withdraw()
            messagebox.showinfo('Information', 'Added possible maximum: ' + str(added))

    def on_add_randomly_clicked(self, event):
        value = self.handle_add_seeds_error(self.input_number_of_seeds.GetValue())
        if value is not None:
            for i in range(value):
                self.image.add_seed_randomly()

    def on_play_clicked(self, event):
        if self.image.cells_taken == 0:
            Tk().wm_withdraw()
            messagebox.showerror('Error', 'Add some seeds before starting the program!')
        elif self.image.cells_taken != self.image.WIDTH * self.image.HEIGHT:
            self.image.paused = False
            self.SetStatusText("Running...")

    def on_pause_clicked(self, event):
        self.image.paused = True
        self.SetStatusText("Paused...")

    def on_reset_clicked(self, event):
        self.image.paused = True
        self.image.restore()
        self.SetStatusText("Paused and restored...")

    def on_clean_clicked(self, event):
        self.image.paused = True
        self.image.clean()
        self.SetStatusText("Paused and cleaned...")

    def on_neighbourhood_selected(self, event):
        self.image.neighbourhood = self.combo.GetValue()

    def on_conditions_selected(self, event):
        self.image.conditions = self.combo_conditions.GetValue()

    def on_set_size_clicked(self, event):
        try:
            self.image.done = True
            self.image.join()
            self.image = image.Image(self,
                                     int(self.input_width.GetValue()),
                                     int(self.input_height.GetValue()),
                                     int(self.input_box_size.GetValue()),
                                     self.combo.GetValue(),
                                     self.combo_conditions.GetValue(),
                                     int(1 / float(self.combo_time.GetValue()[:3])))
            self.image.start()
        except ValueError:
            Tk().wm_withdraw()
            messagebox.showerror('Error', 'Illegal characters! Only integers allowed.')

    def on_time_step_clicked(self, event):
        self.image.time_step = int(1 / float(self.combo_time.GetValue()[:3]))

    def on_exit(self, event):
        self.Close(True)


if __name__ == '__main__':
    app = wx.App()
    frm = MainFrame(None, title='')
    frm.Show()

    app.MainLoop()
