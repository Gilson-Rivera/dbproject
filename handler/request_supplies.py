from flask import jsonify
from dao.request_supplies import RequestedSuppliesDAO


class RequestedSuppliesHandler:
    def build_request_supplies_dict(self, row):
        result = {}
        result['aid'] = row[0]
        result['sid'] = row[1]
        result['request_type'] = row[2]
        result['request_quantity'] = row[3]
        result['request_brand'] = row[4]
        return result

    # def build_RequestedSupplies_attributes(self, aid, sid, request_type, request_quantity, request_brand):
    #     result = {}
    #     result['aid'] = aid
    #     result['sid'] = sid
    #     result['request_type'] = request_type
    #     result['request_quantity'] = request_quantity
    #     result['request_brand'] = request_brand
    #     return result

    def getAllRequestedSupplies(self):
        dao = RequestedSuppliesDAO()
        request_supplies_list = dao.getAllRequestedSupplies()
        result_list = []
        for row in request_supplies_list:
            result = self.build_request_supplies_dict(row)
            result_list.append(result)
        return jsonify(RequestedSupplies=result_list)

    def getRequestedSuppliesByID(self, aid, sid):
        dao = RequestedSuppliesDAO()
        result = dao.getRequestedSuppliesByID(aid, sid)
        # if not row:
        #     return jsonify(Error = "Food Not Found"), 404
        # else:
        #     Food = self.build_Food_dict(row)
        return jsonify(RequestedSupplies=result)

    def searchRequestedSupplies(self, args):
        type = args.get("type")
        dao = RequestedSuppliesDAO()
        requested_supplies_list = []
        if (len(args) == 1) and type:
            requested_supplies_list = dao.getRequestedSuppliesByType(type)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in requested_supplies_list:
            result = self.build_request_supplies_dict(row)
            result_list.append(result)
        return jsonify(RequestedSupplies=result_list)

    # def insertRequestedSupplies(self, form):
    #     print("form: ", form)
    #     if len(form) != 4:
    #         return jsonify(Error = "Malformed post request"), 400
    #     else:
    #         request_type = form['request_type']
    #         request_quantity = form['request_quantity']
    #         request_brand = form['request_brand']
    #
    #         if request_type and request_quantity and request_brand:
    #             dao = RequestedSuppliesDAO()
    #             sid = dao.insert(request_type, request_quantity, request_brand)
    #             result = self.build_RequestedSupplies_attributes(aid, sid, request_type, request_quantity, request_brand)
    #             return jsonify(Part=result), 201
    #         else:
    #             return jsonify(Error="Unexpected attributes in post request"), 400
    #
    # def insertRequestedSuppliesJson(self, json):
    #     cfirstname = json['cfirstname']
    #     clastname = json['clastname']
    #     clocation = json['clocation']
    #     cage = json['cage']
    #     cphone = json['cphone']
    #     if cfirstname and clastname and clocation and cage and cphone:
    #         dao = RequestedSuppliesDAO()
    #         result = dao.insert(cfirstname, clastname, clocation, cage, cphone)
    #         return jsonify(RequestedSupplies=result), 201
    #     else:
    #         return jsonify(Error="Unexpected attributes in post request"), 400
    #

    def deleteRequestedSupplies(self, aid, sid):
        dao = RequestedSuppliesDAO()
        # if not dao.getRequestedSuppliesById(cid):
        #     return jsonify(Error = "Part not found."), 404
        # else:
        result = dao.delete(aid, sid)
        return jsonify(DeleteStatus = result), 200

    def updateRequestedSupplies(self, aid, sid):
        dao = RequestedSuppliesDAO()
        if not dao.getRequestedSuppliesByID(aid, sid):
            return jsonify(Error = "RequestedSupplies not found."), 404
        else:
            return jsonify(dao.getRequestedSuppliesByID(sid, aid)), 201

    # def getRequestedSuppliesById(self, cid):
    #     dao = RequestedSuppliessDAO()
    #     row = dao.getRequestedSuppliesById(cid)
    #     if not row:
    #         return jsonify(Error="Part Not Found"), 404
    #     else:
    #         RequestedSupplies = self.build_RequestedSupplies_dict(row)
    #         return jsonify(RequestedSupplies=RequestedSupplies)
    #
    # def searchRequestedSuppliess(self, args):
    #     name = args.get("name")
    #     dao = RequestedSuppliessDAO()
    #     RequestedSuppliess_list = []
    #     if (len(args) == 1) and name:
    #         RequestedSuppliess_list = dao.getRequestedSuppliesByName(name)
    #     else:
    #         return jsonify(Error = "Malformed query string"), 400
    #     result_list = []
    #     for row in RequestedSuppliess_list:
    #         result = self.build_RequestedSupplies_dict(row)
    #         result_list.append(result)
    #     return jsonify(RequestedSuppliess=result_list)
    #
    #
    # def insertRequestedSupplies(self, form):
    #     print("form: ", form)
    #     if len(form) != 4:
    #         return jsonify(Error = "Malformed post request"), 400
    #     else:
    #         cfirstname = form['cfirstname']
    #         clastname = form['clastname']
    #         clocation = form['clocation']
    #         cage = form['cage']
    #         cphone = form['cphone']
    #
    #         if cfirstname and clastname and clocation and cage and cphone:
    #             dao = RequestedSuppliessDAO()
    #             cid = dao.insert(cfirstname, clastname, clocation, cage, cphone)
    #             result = self.build_RequestedSupplies_attributes(cid, cfirstname, clastname, clocation, cage, cphone)
    #             return jsonify(Part=result), 201
    #         else:
    #             return jsonify(Error="Unexpected attributes in post request"), 400
    #
    # def insertRequestedSuppliesJson(self, json):
    #     cfirstname = json['cfirstname']
    #     clastname = json['clastname']
    #     clocation = json['clocation']
    #     cage = json['cage']
    #     cphone = json['cphone']
    #     if cfirstname and clastname and clocation and cage and cphone:
    #         dao = RequestedSuppliessDAO()
    #         result = dao.insert(cfirstname, clastname, clocation, cage, cphone)
    #         return jsonify(RequestedSupplies=result), 201
    #     else:
    #         return jsonify(Error="Unexpected attributes in post request"), 400
    #
    # def deleteRequestedSupplies(self, cid):
    #     dao = RequestedSuppliessDAO()
    #     # if not dao.getRequestedSuppliesById(cid):
    #     #     return jsonify(Error = "Part not found."), 404
    #     # else:
    #     result = dao.delete(cid)
    #     return jsonify(DeleteStatus = result), 200
    #
    # def updateRequestedSupplies(self, cid, form):
    #     dao = RequestedSuppliessDAO()
    #     if not dao.getRequestedSuppliesById(cid):
    #         return jsonify(Error = "RequestedSupplies not found."), 404
    #     else:
    #         return jsonify(dao.getRequestedSuppliesById(cid)), 201





