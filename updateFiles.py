class updateFiles:
    def __init__(self, backend, base):
        self.backend = backend
        self.base = base
        directory = self.backend + "/" + self.backend + "/"
        self.settingsFilePath = directory + "settings.py"
        self.URLsFilePath = directory + "urls.py"
        self.tab = '\t'
        self.nextLine = '\n'

    def updateSettingsFile(self):
        with open(self.settingsFilePath, 'r+') as file:
            settingsFileData = file.readlines()

        lineNo = None
        foundPosition = False
        for index, line in enumerate(settingsFileData):
            line = line.strip()
            if line == "INSTALLED_APPS = [":
                foundPosition = True
            if line == "]" and foundPosition:
                lineNo = index
                break
        
        if foundPosition == False:
            print("error in" + self.settingsFilePath + ": Unable to find INSTALLED_APPS FIELD")
            return

        restApp = "'rest_framework',"
        baseApp = "'" + self.base + ".apps." + self.base.title() + "Config',"

        settingsFileData.insert(lineNo, self.tab + restApp + self.nextLine)
        settingsFileData.insert(lineNo + 1, self.tab + baseApp + self.nextLine)

        with open(self.settingsFilePath,'w') as file:
            file.write(''.join(settingsFileData))

    def updateURLsFile(self):
        with open(self.URLsFilePath, 'r+') as file:
            URLsFileData = file.readlines()

        includeLineNo = None
        pathLineNo = None
        foundIncludePosition = False
        foundPathPosition = False

        for index, line in enumerate(URLsFileData):
            line = line.strip()
            if line == "urlpatterns = [":
                foundIncludePosition = True
                includeLineNo = index
                break

        for index, line in enumerate(URLsFileData):
            line = line.strip()
            if line == "]":
                foundPathPosition = True
                pathLineNo = index
                break

        if foundIncludePosition == False or foundPathPosition == False: 
            print("error in" + self.URLsFilePath + ": Unable to find urlpatterns FIELD")
            return
        
        if includeLineNo == 0:
            includeLineNo = 1

        importInclude = "from django.urls import include"
        includePath = "path('api/',include('base.urls')),"

        URLsFileData.insert(includeLineNo - 1, importInclude + self.nextLine)
        URLsFileData.insert(pathLineNo + 1, self.tab + includePath + self.nextLine)

        with open(self.URLsFilePath,'w') as file:
            file.write(''.join(URLsFileData))

