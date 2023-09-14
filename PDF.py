from fpdf import FPDF


class PDF(FPDF):
    pass

    def logo(self, name, x, y, w, h):
        self.image(name, x, y, w, h)

    def texts(self, name):
        with open(name, 'rb') as xy:
            txt = xy.read().decode('latin-1')
        self.set_xy(10.0, 80.0)
        self.set_text_color(00.0, 32, 250)
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 0, txt)

    def titles(self, title):
        self.set_xy(10.0, 80.0)
        self.set_text_color(00.0, 32, 250)
        self.set_font('Arial', '', 12)
        self.cell(w=210.0, h=40.0, align='C', txt=title, border=0)


pdf = PDF(orientation='P', unit='mm', format='a5')
pdf.add_page()
pdf.logo('Logo2.png', 0, 0, 60, 60)
pdf.texts('test.txt')
pdf.titles('Ticket')
pdf.set_author(author='Mike')
pdf.output(name='test.pdf')
