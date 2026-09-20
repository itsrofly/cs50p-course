from fpdf import FPDF

class PDF(FPDF):
    def header(self, orientation="P", unit="mm", format="A4"):
        self.image("shirtificate.png", x=0, y=50)

        self.ln(20)
        self.set_font("helvetica", "B", size=40)
        self.set_text_color(1, 1, 1)
        self.cell(0,0,'CS50 Shirtificate', align="C")


        self.ln(100)
        self.set_font("helvetica", "B", size=30)
        self.set_text_color(255, 255, 255)
        self.cell(0,0,f"{self.name} took CS50", align="C")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid Name")
        self._name = name



def main():
    pdf = PDF()
    pdf.name = input("Name: ")
    name = pdf.name
    name = name.replace(" ","_")
    pdf.add_page()
    pdf.output(f"shirtificate.pdf")


if __name__ == "__main__":
    main()