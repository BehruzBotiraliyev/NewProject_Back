from modeltranslation.translator import translator, TranslationOptions
from app.models import News, About, Employees, Services, ServiceType, EmployeePositions


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


class EmployeesTranslationOptions(TranslationOptions):
    fields = ('fullname', 'address')


class EmployeePositionsTranslationOptions(TranslationOptions):
    fields = ('title', 'attr')


class ServicesTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


class ServiceTypeTranslationOptions(TranslationOptions):
    fields = ('title', 'attr')


translator.register(News, NewsTranslationOptions)
translator.register(About, AboutTranslationOptions)
translator.register(Employees, EmployeesTranslationOptions)
translator.register(EmployeePositions, EmployeePositionsTranslationOptions)
translator.register(Services, ServicesTranslationOptions)
translator.register(ServiceType, ServiceTypeTranslationOptions)
