import fitz
import pyperclip

def checkClause(filename):
    with open(filename, 'rb') as pdf_file:
        pdf_reader = fitz.open(pdf_file)
        text = ''
        pages = []
        pointer = 0
        for page_num in range(pdf_reader.page_count):
            page = pdf_reader.load_page(page_num)
            tx = page.get_text().replace("\n", " ")
            text += tx
            pages += [pointer]
            pointer += len(tx)
        pages+=[pointer]

    clauses = {}
    clauses["Membership Clause"] = "Only currently registered students, faculty, and staff may be active members in a registered student organization. Only active members may vote or hold office."
    clauses["Anti-haze Clause"] = "We will not haze according to California State Law."
    clauses['Non-discrimination Clause'] = "We will not restrict membership based upon race, color, national origin, religion, sex, gender identity, pregnancy (including pregnancy, childbirth, and medical conditions related to pregnancy or childbirth), physical or mental disability, medical condition (cancer related or genetic characteristics), ancestry, marital status, age, sexual orientation, citizenship, or service in the uniformed services (including membership, application for membership, performance of service, application for service, or obligation for service in the uniformed services)."
    clauses['Amendments Clause (address needs updating) ie. what was formerly LEAD Center and 432 Eshleman is now outdated. Please edit your Amendments clause to state →> "All amendments, additions or deletions to this document must be filed with the OASIS Center at oasis.center@berkeley.edu, or OASIS Center at 312 Eshleman Hall.'] = "All amendments, additions or deletions to this document must be filed with the OASIS Center at oasis.center@berkeley.edu, or OASIS Center at 312 Eshleman Hall. "
    def diss(text):
        base = "If the organization is ASUC or GA Sponsored, all unspent ASUC funds shall return to the ASUC; all Graduate Assembly funds shall return to the Graduate Assembly. If the organization is defunct for five (5) or more years, any privately obtained funds (including any funds left in miscellaneous accounts) shall be "
        a1 = "donated to the ASUC"
        a2 = "donated to the following nonprofit organization: "
        a22 = "In the event that the designated nonprofit organization no longer exists or has ceased to be a nonprofit, then the unspent funds shall be donated to the ASUC."
        if base+a1 in text:
            num = text.index(base+a1)
            for i in range(len(pages)):
                if pages[i] >= num:
                    return i
            return text.index(base+a1)
        elif base+a2 in text and a22 in text:
            num = text.index(base+a2)
            for i in range(len(pages)):
                if pages[i] >= num:
                    return i
        else:
            return -1
    clauses["Dissolution Clause"] = diss

    missing = []

    for j in clauses:
        x = clauses[j]
        if type(x) == str:
            num = -1
            if x in text:
                num = text.index(x)
            else:
                print("missing clause", j[:min(len(j), j.index("Clause")+6)])
                missing.append(j)
                continue
            for i in range(len(pages)):
                if pages[i] >= num:
                    print(j[:min(len(j), j.index("Clause")+6)]+': page '+str(i))
                    break
        else:
            i = x(text)
            if i > 0:
                print(j[:min(len(j), j.index("Clause")+6)]+': page '+str(i))
            else:
                print("missing clause", j[:min(len(j), j.index("Clause")+6)])
                missing.append(j)
                continue

    print("------------------------------")
    outtext = "Approved"
    x = len(missing)
    need = ", ".join(missing)
    if x:
        outtext = """Your RSO Constitution requires an updated: """+str(x)+""" clauses—>
        Clauses Needed: """+need
        pyperclip.copy(outtext)
    print(outtext)