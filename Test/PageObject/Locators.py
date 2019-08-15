
class Locator(object):

#HomePage Locators
    kredit = "//img[@alt='Kredit']"
#CreditInfo Locators
    money = "amount"
    purpose="select-purpose"
    time="//div[@id='select-term']"
    tagLi="li"
    usage ="//li[@data-testid='Betriebsmittel']"
    runningTime ="//li[@data-testid='6 Monate']"
    continueButton ="//button/span[contains(text(),'Weiter')]"
#CompanySelection Locators
    company ="companyName"
    search="//button/span[contains(text(),'Unternehmen')]"
    selectCompany="//div/h3[contains(text(),'FinComp')]"
#Registration Locators
    gender="//input[@value='f']"
    fName="firstName"
    sName="lastName"
    emailAdd="email"
    buisUsage="select-businessRelation"
    usedBy="//li[contains(text(), 'Ihren Arb')]"
    register="//button/span[contains(text(),'Kost')]"


