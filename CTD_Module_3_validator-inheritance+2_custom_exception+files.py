# %% [markdown]
# CTD Module 3 mein P.1 (Composition) aur P.4 (Excipients) sections validate karne hain. Base class banao CTDSection jisme attributes hon — section_id, drug_name, version aur method validate() jo sirf pass kare. 2 custom exceptions banao — MissingDataError aur VersionError. Child class banao CompositionSection(CTDSection) jisme extra attributes hon — ingredients list, batch_size. Override karo validate() — agar ingredients khali ho toh MissingDataError, agar version "2.0" se kam ho toh VersionError raise karo. Valid sections "ctd_validated.txt" mein save karo. 3 sections test karo.

# %%
import logging

logging.basicConfig(
    filename="ctd_validated.txt",
    level=logging.DEBUG,
    format="%(asctime)s — %(levelname)s — %(message)s"
)

#mking of 2 custom exceptions for the ctd validation process
#1
class MissingDataError(Exception):
    pass
#2
class VersionError(Exception):
    pass

#core function to validate the ctd file
def CTD_Sections():
    def __init__(self, section_id, drug_name, version):
        self.section_id = section_id
        self.drug_name = drug_name
        self.version = version

    def validate(self):
        pass    #child class will override it.

    #how the function will e shon 
    def __str__(self):
        return f"Section ID: {self.section_id}, Drug Name: {self.drug_name}, Version: {self.version}"

#creating a child class 
class CTD_Sections:
    def __init__(self, section_id, drug_name, version):
        self.section_id = section_id
        self.drug_name = drug_name
        self.version = version

    def validate(self):
        pass    # child class will override it.

    def __str__(self):
        return f"Section ID: {self.section_id}, Drug Name: {self.drug_name}, Version: {self.version}"

class CompositionSection(CTD_Sections):
    def __init__(self, section_id, drug_name, version, ingredients, batch_size):
        super().__init__(section_id, drug_name, version)
        self.ingredients = ingredients
        self.batch_size = batch_size

    def validate(self):
        print(f"\nvalidating Composition Section for {self.section_id}...")

        try:
            if not self.ingredients:
                raise MissingDataError(f"Missing ingredients in section {self.section_id}")

            if float(self.version) < 2.0:
                raise VersionError(f"Version {self.version} is not supported for section {self.section_id}")

            msg = (f"VALID | {self.section_id} | {self.drug_name} | "
                   f"v{self.version} | Ingredients: {self.ingredients}")
            logging.info(msg)
            print(f"{self.section_id} is valid saved to file.")

        except MissingDataError as e:
            logging.warning(f"MISSING DATA | {self.section_id} | {e}")
            print(f"ERROR : {e}")

        except VersionError as e:
            logging.error(f"VERSION ERROR | {self.section_id} | {e}")
            print(f"ERROR : {e}")




#testing some examples;
sections = [
    CompositionSection(
        "P.1.001", "Metformin 500mg", "2.1",
        ["Metformin HCl", "Lactose", "MgStearate"], 100000
    ),   
    CompositionSection(
        "P.1.002", "Aspirin 75mg", "1.5",
        ["Aspirin", "Starch"], 50000
    ),   
    CompositionSection(
        "P.1.003", "Insulin 100IU", "2.0",
        [], 10000
    ),  
]


for section in sections:
    print(section)
    section.validate()




