import tkinter as tk


#region Pencere Ekleme
# Bu fonksiyon ile yeni pencereler oluşturabiliriz
def create_window(**kwargs):
    """
    Örnek kullanım

    Pencere_1 = create_window(width=500, height=400, title="Plc Kontrol", bg='light blue')
    """

    root = tk.Tk()

    # Ekran çözünürlüğünü al ve pencere boyutunu ayarla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = kwargs.get('width', 800)
    height = kwargs.get('height', 600)
    x_offset = int((screen_width - width) / 2)
    y_offset = int((screen_height - height) / 2)
    root.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

    # Pencere başlığını ve arka plan rengini ayarla
    title = kwargs.get('title', 'Tkinter Penceresi')
    bg_color = kwargs.get('bg', 'white')
    root.title(title)
    root.configure(bg=bg_color)

    return root

# Pencere oluştur
# Pencere_1 = create_window(width=500, height=400, title="Plc Kontrol", bg='light blue')

#endregion

#region Buton Ekleme

# Bu fonksiyon ile yeni butonlar oluşturabiliriz
def add_button(**kwargs):

    """Örnek kullanım  | Bu verilerin hepsi girilmek zorunda değil. Zaten içeride hepsinin default ayarları var.
    Btn_Name = add_button(pencere=Pencere_1, text="Bağlantı Kur", bg="gray", fg="black", font=("Arial", 11, "bold"),
                             borderwidth=2, relief="ridge", cursor="hand2",
                             button_x=0, button_y=0, button_width=200, button_height=100,
                             on_click={'action': lambda: Buton_Event(Btn_Name)}) /def ile bir event oluştur"""

    root = kwargs.get('pencere')
    text = kwargs.get('text', 'Buton')
    button_x = kwargs.get('button_x', 0)
    button_y = kwargs.get('button_y', 0)
    button_width = kwargs.get('button_width', None)
    button_height = kwargs.get('button_height', None)
    click_event = kwargs.get('on_click')

    # Varsayılan buton konfigürasyonları
    default_button_config = {
        'bg': 'gray',
        'fg': 'white',
        'font': ('Helvetica', 12, 'bold'),
        'borderwidth': 3,
        'relief': 'ridge',
        'cursor': 'hand2'
    }

    # kwargs içinde belirtilen özelliklerle varsayılanları birleştir
    button_config = {**default_button_config, **kwargs}

    # Buton oluştur ve konfigüre et
    button = tk.Button(root, text=text)
    button.config(**{k: v for k, v in button_config.items() if
                     k not in ['pencere', 'text', 'on_click', 'button_x', 'button_y', 'button_width', 'button_height']})
    button.place(x=button_x, y=button_y, width=button_width, height=button_height)

    # Buton komutunu ayarla
    if click_event and 'action' in click_event:
        button.config(command=click_event['action'])

    return button


# Her buton için bu şekilde eventler oluşturmak gerekir.
# def Btn_Connect_Click(button):
#     print(f"Giriş değeri: {Entry_1.get()}")


    # if button.cget('bg') == 'red':
    #     button.config(bg='green')
    # else:
    #     button.config(bg='red')

# Buton ekle
# Btn_Connect = add_button(pencere=Pencere_1, text="Bağlantı Kur", bg="gray", fg="black", font=("Arial", 11, "bold"),
#                          borderwidth=2, relief="ridge", cursor="hand2",
#                          button_x=0, button_y=0, button_width=200, button_height=100,
#                          on_click={'action': lambda: Btn_Connect_Click(Btn_Connect)})
#endregion

#region Label Ekleme

def add_label(**kwargs):
    root = kwargs.get('pencere')
    text = kwargs.get('text', '')
    label_x = kwargs.get('label_x', 0)
    label_y = kwargs.get('label_y', 0)
    label_width = kwargs.get('label_width', None)
    label_height = kwargs.get('label_height', None)

    # Varsayılan label konfigürasyonları
    default_label_config = {
        'bg': 'lightgray',
        'fg': 'black',
        'font': ('Arial', 12),
        'anchor': 'center'
    }

    # kwargs içinde belirtilen özelliklerle varsayılanları birleştir
    label_config = {**default_label_config, **kwargs}

    # Label oluştur ve konfigüre et
    label = tk.Label(root, text=text)
    label.config(**{k: v for k, v in label_config.items() if k not in ['pencere', 'text', 'label_x', 'label_y', 'label_width', 'label_height']})
    label.place(x=label_x, y=label_y, width=label_width, height=label_height)

    return label

# Label eklemek için kullanımı
# Lbl_Info = add_label(pencere=Pencere_1, text="Bağlantı Bilgisi:", bg="lightblue", fg="darkblue",
#                      font=("Helvetica", 10, "italic"), label_x=50, label_y=150, label_width=200)

#endregion

#region Label Ekleme
def add_entry(**kwargs):
    root = kwargs.get('pencere')
    entry_x = kwargs.get('entry_x', 0)
    entry_y = kwargs.get('entry_y', 0)
    entry_width = kwargs.get('entry_width', 20)
    entry_height = kwargs.get('entry_height', None)

    # Varsayılan entry konfigürasyonları
    default_entry_config = {
        'bg': 'white',
        'fg': 'black',
        'font': ('Arial', 12)
    }

    # kwargs içinde belirtilen özelliklerle varsayılanları birleştir
    entry_config = {**default_entry_config, **kwargs}

    # Entry oluştur ve konfigüre et
    entry = tk.Entry(root)
    entry.config(**{k: v for k, v in entry_config.items() if k not in ['pencere', 'entry_x', 'entry_y', 'entry_width', 'entry_height']})
    entry.place(x=entry_x, y=entry_y, width=entry_width, height=entry_height)

    return entry

# Entry eklemek için kullanımı
# Entry_1 = add_entry(pencere=Pencere_1, bg="lightyellow", fg="darkblue",
#                     font=("Helvetica", 14), entry_x=50, entry_y=100, entry_width=150)


# Pencere_1.mainloop()


#endregion




def WindowStart(Pencere):
    Pencere.mainloop()


