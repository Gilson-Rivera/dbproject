from flask import jsonify
from dao.administrators import AdministratorsDAO


class AdministratorHandler:
    def build_administrator_dict(self, row):
        result = {}
        result['aid'] = row[0]
        result['afirstname'] = row[1]
        result['alastname'] = row[2]
        result['alocation'] = row[3]
        result['a_age'] = row[4]
        result['aphone'] = row[5]
        return result

    def build_administrator_attributes(self, aid, afirstname, alastname, alocation, a_age, aphone):
        result = {}
        result['aid'] = aid
        result['afirstname'] = afirstname
        result['alastname'] = alastname
        result['alocation'] = alocation
        result['a_age'] = a_age
        result['aphone'] = aphone
        return result

    def getAllAdministrators(self):
        dao = AdministratorsDAO()
        administrators_list = dao.getAllAdministrators()
        result_list = []
        for row in administrators_list:
            result = self.build_administrator_dict(row)
            result_list.append(result)
        return jsonify(Administrators=result_list)

    def getAdministratorById(self, cid):
        dao = AdministratorsDAO()
        row = dao.getAdministratorById(cid)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            administrator = self.build_administrator_dict(row)
            return jsonify(Administrator=administrator)

    def searchAdministrators(self, args):
        name = args.get("name")
        dao = AdministratorsDAO()
        administrators_list = []
        if (len(args) == 1) and name:
            administrators_list = dao.getAdministratorByName(name)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in administrators_list:
            result = self.build_administrator_dict(row)
            result_list.append(result)
        return jsonify(Administrators=result_list)


    def insertAdministrator(self, form):
        print("form: ", form)
        if len(form) != 4:
            return jsonify(Error = "Malformed post request"), 400
        else:
            afirstname = form['afirstname']
            alastname = form['alastname']
            alocation = form['alocation']
            a_age = form['a_age']
            aphone = form['aphone']

            if afirstname and alastname and alocation and a_age and aphone:
                dao = AdministratorsDAO()
                aid = dao.insert(afirstname, alastname, alocation, a_age, aphone)
                result = self.build_administrator_attributes(aid, afirstname, alastname, alocation, a_age, aphone)
                return jsonify(Part=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertAdministratorJson(self, json):
        afirstname = json['afirstname']
        alastname = json['alastname']
        alocation = json['alocation']
        a_age = json['a_age']
        aphone = json['aphone']
        if afirstname and alastname and alocation and a_age and aphone:
            dao = AdministratorsDAO()
            aid = dao.insert(afirstname, alastname, alocation, a_age, aphone)
            result = self.build_administrator_attributes(aid, afirstname, alastname, alocation, a_age, aphone)
            return jsonify(Administrator=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteAdministrator(self, aid):
        dao = AdministratorsDAO()
        if not dao.getAdministratorById(aid):
            return jsonify(Error = "Part not found."), 404
        else:
            dao.delete(aid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateAdministrator(self, aid, form):
        dao = AdministratorsDAO()
        if not dao.getAdministratorById(aid):
            return jsonify(Error = "Administrator not found."), 404
        else:
            return jsonify(dao.getAdministratorById(aid)), 201
