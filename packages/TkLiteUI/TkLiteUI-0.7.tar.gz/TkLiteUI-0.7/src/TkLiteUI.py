"""
TkLiteUI as tl
    Öncelikle tl modülünden ui sınıfını kullanarak bir örnek oluşturun
----------------
ui = tl.ui()
----------------
.
.
--------------------
Yazar: Adem Ulker
--------------------
"""
import tkinter as tk


class ui:
    """
                UI sınıfı, Tkinter tabanlı bir grafik kullanıcı arayüzü (GUI) uygulaması için temel işlevler sağlar.
                Bu sınıfın bir örneği, farklı GUI bileşenleri oluşturmak için kullanılır.

                Özellikler:
                ----------------
                - FirstWindow (bool): İlk Tkinter penceresinin oluşturulup oluşturulmadığını takip eder.
                                      Bu, birden fazla pencere yönetiminde kullanılır.

                Bu sınıf, pencere oluşturma, buton ekleme ve diğer widget yönetimi gibi işlevleri içerir.

                --------------------
                Yazar: Adem Ulker
                --------------------
                """
    def __init__(self):
        self.FirstWindow = False

    # region Pencere Ekleme
    # Bu fonksiyon ile yeni pencereler oluşturabiliriz
    # İlk pencere oluşturuldu mu diye kontrol etmek için bir flag (işaretçi) kullanın
    def create_window(self, **kwargs):
        """
            Belirtilen özelliklere göre bir Tkinter penceresi oluşturur.

            İlk pencere daha önce oluşturulmuşsa, bir 'Toplevel' penceresi oluşturur ve gerekirse gizler.
            İlk pencere henüz oluşturulmamışsa, bir 'Tk' ana penceresi oluşturur.

            Parametreler:
            ----------------
            width (int): Pencerenin genişliği. Varsayılan değer 400.
            height (int): Pencerenin yüksekliği. Varsayılan değer 300.
            title (str): Pencerenin ismi. Varsayılan değer 'Türkiye'.
            bg (str): Arka plan rengi. Varsayılan değer 'white'.
            is_primary (bool): Eğer True ise, pencere başlangıçta gizlenir. Varsayılan False.

            Örnek Kullanım:
            ----------------
            pencere = create_window(width=500, height=400, title="Türkiye", bg='light blue', is_primary=True)

            --------------------
            Yazar: Adem Ulker
            --------------------
            """

        # İlk pencere oluşturulduysa Toplevel kullan, değilse Tk
        if self.FirstWindow:
            root = tk.Toplevel()
            root.protocol("WM_DELETE_WINDOW", root.withdraw)
            if kwargs.get('is_primary', False):
                root.withdraw()
        else:
            root = tk.Tk()
            self.FirstWindow = True  # İlk pencere oluşturuldu olarak işaretle

        # Pencere özelliklerini ayarla
        width = kwargs.get('width', 400)
        height = kwargs.get('height', 300)
        title = kwargs.get('title', 'Türkiye')
        bg = kwargs.get('bg', 'white')

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_offset = (screen_width - width) // 2
        y_offset = (screen_height - height) // 2
        root.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

        root.title(title)
        root.configure(bg=bg)

        return root

    #  ui = ui() // En başta oluşturulması gereken sınıf
    # Pencere oluştur
    # Pencere_1 = ui.create_window(width=500, height=400, title="Plc Kontrol", bg='light blue')

    # endregion

    # region Buton Ekleme

    # Bu fonksiyon ile yeni butonlar oluşturabiliriz
    def add_button(self, **kwargs):
        """
        Belirtilen özelliklere göre bir Tkinter butonu oluşturur ve konumlandırır.

        Parametreler:
        ----------------
        pencere (WindowName): Butonun ekleneceği pencere.
        text (str): Buton üzerinde görünecek metin.
        button_x (int): Butonun x koordinatı.
        button_y (int): Butonun y koordinatı.
        button_width (int, opsiyonel): Butonun genişliği.
        button_height (int, opsiyonel): Butonun yüksekliği.

        on_click (dict, opsiyonel): Butona tıklandığında çağrılacak fonksiyonu belirtir.
        'action' anahtarı, bir lambda ifadesi veya çağrılabilir bir nesneyi (fonksiyon ya da metot) içerir.
        Örneğin: on_click={'action': lambda: buton_fonksiyonu()} veya
        on_click={'action': fonksiyon_adi} şeklinde kullanılabilir.

        Örnek Kullanım:
        ----------------
        Buton_Name = ui.add_button(pencere=WindowName, text="Buton", bg="gray", fg="black",
                                font=("Arial", 11, "bold"), borderwidth=2, relief="ridge", cursor="hand2",
                                button_x=0, button_y=0, button_width=200, button_height=100,
                                on_click={'action': lambda: Buton_Event(Buton_Name)})

        --------------------
        Yazar: Adem Ulker
        --------------------
        """

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
                         k not in ['pencere', 'text', 'on_click', 'button_x', 'button_y', 'button_width',
                                   'button_height']})
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
    # endregion

    # region Label Ekleme

    def add_label(self, **kwargs):
        """
        Belirtilen özelliklere göre bir Tkinter etiketi (Label) oluşturur ve konumlandırır.

        Parametreler:
        ----------------
        pencere (WindowName): Label'in ekleneceği pencere.
        text (str): Label metni.
        label_x (int): Label x koordinatı.
        label_y (int): Label y koordinatı.
        label_width (int, opsiyonel): Label genişliği.
        label_height (int, opsiyonel): Label yüksekliği.
        bg (str, opsiyonel): Arka plan rengi.
        fg (str, opsiyonel): Yazı rengi.
        font (tuple, opsiyonel): Yazı tipi ve boyutu.

        Örnek Kullanım:
        ----------------
        Label_1 = ui.add_label(pencere=WindowName, text="Text", bg="lightblue", fg="darkblue",
                            font=("Helvetica", 10, "italic"), label_x=50, label_y=150, label_width=200)

        --------------------
        Yazar: Adem Ulker
        --------------------
        """

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
        label.config(**{k: v for k, v in label_config.items() if
                        k not in ['pencere', 'text', 'label_x', 'label_y', 'label_width', 'label_height']})
        label.place(x=label_x, y=label_y, width=label_width, height=label_height)

        return label

    # Label eklemek için kullanımı
    # Lbl_Info = add_label(pencere=Pencere_1, text="Bağlantı Bilgisi:", bg="lightblue", fg="darkblue",
    #                      font=("Helvetica", 10, "italic"), label_x=50, label_y=150, label_width=200)

    # endregion

    # region Entry Ekleme
    def add_entry(self, **kwargs):
        """
        Belirtilen özelliklere göre bir Tkinter giriş kutusu (entry) oluşturur ve konumlandırır.

        Parametreler:
        ----------------
        pencere (WindowName): Giriş kutusunun ekleneceği pencere.
        entry_x (int): Giriş kutusunun x koordinatı.
        entry_y (int): Giriş kutusunun y koordinatı.
        entry_width (int): Giriş kutusunun genişliği.
        entry_height (int, opsiyonel): Giriş kutusunun yüksekliği.
        bg (str, opsiyonel): Arka plan rengi.
        fg (str, opsiyonel): Yazı rengi.
        font (tuple, opsiyonel): Yazı tipi ve boyutu.

        Örnek Kullanım:
        ----------------
        EntryName = ui.add_entry(pencere=WindowName, bg="lightyellow", fg="darkblue",
                              font=("Helvetica", 14), entry_x=50, entry_y=100, entry_width=150)

        --------------------
        Yazar: Adem Ulker
        --------------------
        """
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
        entry.config(**{k: v for k, v in entry_config.items() if
                        k not in ['pencere', 'entry_x', 'entry_y', 'entry_width', 'entry_height']})
        entry.place(x=entry_x, y=entry_y, width=entry_width, height=entry_height)

        return entry

    # Entry eklemek için kullanımı
    # Entry_1 = add_entry(pencere=Pencere_1, bg="lightyellow", fg="darkblue",
    #                     font=("Helvetica", 14), entry_x=50, entry_y=100, entry_width=150)

    # Pencere_1.mainloop()

    # endregion

    def StartMainWindow(self, Pencere):
        """
        Ana pencereyi başlatır.

        Parametreler:
        ----------------
        StartMainWindow(windowName): Başlatılacak ana Tkinter penceresi.

        Örnek Kullanım:
        ----------------
        ui.StartMainWindow(MainWindowName)

        --------------------
        Yazar: Adem Ulker
        --------------------
        """
        Pencere.mainloop()

    def CloseMainWindow(self, Pencere):
        """
        Ana pencereyi kapatır ve kaynakları serbest bırakır.

        Parametreler:
        ----------------
        CloseMainWindow(windowName): Kapatılacak ana Tkinter penceresi.

        Örnek Kullanım:
        ----------------
        ui.CloseMainWindow(MainWindowName)

        --------------------
        Yazar: Adem Ulker
        --------------------
        """
        Pencere.destroy()

    def ShowSubWindow(self, pencere):
        """
        Yardımcı pencereyi gösterir.

        Parametreler:
        ----------------
        pencere (windowName): Gösterilecek yardımcı Tkinter penceresi.

        Örnek Kullanım:
        ----------------
        ui.ShowSubWindow(SubWindowName)

        --------------------
        Yazar: Adem Ulker
        --------------------
        """
        pencere.deiconify()

    def HideSubWindow(self, pencere):
        """
        Yardımcı pencereyi gizler.

        Parametreler:
        ----------------
        ui.HideSubWindow(windowName): Gizlenecek yardımcı Tkinter penceresi.

        Örnek Kullanım:
        ----------------
        HideSubWindow(SubWindowName)

        --------------------
        Yazar: Adem Ulker
        --------------------
        """
        pencere.withdraw()
