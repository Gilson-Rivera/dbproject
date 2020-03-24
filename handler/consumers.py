from flask import jsonify
from dao.consumer import ConsumersDAO


class ConsumerHandler:
    # def build_part_dict(self, row):
    #     result = {}
    #     result['pid'] = row[0]
    #     result['pname'] = row[1]
    #     result['pmaterial'] = row[2]
    #     result['pcolor'] = row[3]
    #     result['pprice'] = row[4]
    #     return result
    #
    # def build_supplier_dict(self, row):
    #     result = {}
    #     result['sid'] = row[0]
    #     result['sname'] = row[1]
    #     result['scity'] = row[2]
    #     result['sphone'] = row[3]
    #     return result
    #
    # def build_part_attributes(self, pid, pname, pcolor, pmaterial, pprice):
    #     result = {}
    #     result['pid'] = pid
    #     result['pname'] = pname
    #     result['pmaterial'] = pcolor
    #     result['pcolor'] = pmaterial
    #     result['pprice'] = pprice
    #     return result

    def getAllConsumers(self):
        dao = ConsumersDAO()
        result_list = dao.getAllConsumers()
        return jsonify(Consumers=result_list)

    def getConsumerById(self, cid):
        dao = ConsumersDAO()
        result = dao.getConsumerById(cid)
        return jsonify(Consumers=result)

    def searchConsumers(self, args):
        name = args.get("name")
        dao = ConsumersDAO()
        results_list = []
        if (len(args) == 1) and name:
            results_list = dao.getConsumerByName(name)
        else:
            results_list = dao.searchConsumerBeta()
        return jsonify(Consumers=results_list)


    # def insertPart(self, form):
    #     print("form: ", form)
    #     if len(form) != 4:
    #         return jsonify(Error = "Malformed post request"), 400
    #     else:
    #         pname = form['pname']
    #         pprice = form['pprice']
    #         pmaterial = form['pmaterial']
    #         pcolor = form['pcolor']
    #         if pcolor and pprice and pmaterial and pname:
    #             dao = PartsDAO()
    #             pid = dao.insert(pname, pcolor, pmaterial, pprice)
    #             result = self.build_part_attributes(pid, pname, pcolor, pmaterial, pprice)
    #             return jsonify(Part=result), 201
    #         else:
    #             return jsonify(Error="Unexpected attributes in post request"), 400

    def insertConsumerJson(self, json):
        cfirstname = json['cfirstname']
        clastname = json['clastname']
        clocation = json['clocation']
        c_age = json['c_age']
        if cfirstname and clastname and clocation and c_age:
            dao = ConsumersDAO()
            result = dao.insert(cfirstname, clastname, clocation, c_age)
            return jsonify(Consumer=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteConsumer(self, cid):
        dao = ConsumersDAO()
        if not dao.getConsumerById(cid):
            return jsonify(Error = "Part not found."), 404
        else:
            dao.delete(cid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateConsumer(self, cid, form):
        dao = ConsumersDAO()
        if not dao.getConsumerById(cid):
            return jsonify(Error = "Consumer not found."), 404
        else:
            return jsonify(dao.getConsumerById(cid)), 201

    # def build_part_counts(self, part_counts):
    #     result = []
    #     #print(part_counts)
    #     for P in part_counts:
    #         D = {}
    #         D['id'] = P[0]
    #         D['name'] = P[1]
    #         D['count'] = P[2]
    #         result.append(D)
    #     return result
    #
    # def getCountByPartId(self):
    #     dao = ConsumersDAO()
    #     result = dao.getCountByPartId()
    #     #print(self.build_part_counts(result))
    #     return jsonify(PartCounts = self.build_part_counts(result)), 200



