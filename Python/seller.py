from flask import *
from database import *

seller=Blueprint('seller',__name__)

@seller.route('/sellerhome')
def sellerhome():
	return render_template("sellerhome.html")

@seller.route('/seller_view_quality',methods=['get','post'])
def seller_view_quality():
	data={}
	q="select * from quality"
	res=select(q)
	data['quality']=res
	return render_template("seller_view_quality.html",data=data)

@seller.route('/seller_manage_stock',methods=['get','post'])
def seller_manage_stock():
	data={}
	selid=session['selid']
	id=request.args['id']
	selid=session['selid']
	if 'submit' in request.form:
		quant=request.form['quantity']
		stype=request.form['stype']
		q="insert into stock values(null,'%s','%s','%s','%s')"%(id,selid,quant,stype)
		insert(q)
		return redirect(url_for('seller.seller_manage_stock',id=id))

	
	q="select * from stock where Quality_id='%s' and Seller_id='%s'"%(id,selid)
	res=select(q)
	data['quantity']=res


	return render_template("seller_manage_stock.html",data=data)


@seller.route('/seller_view_stocks')
def seller_view_stocks():
	data={}
	selid=session['selid']
	q="select * from stock inner join quality using(Quality_id) where Seller_id='%s'"%(selid)
	res=select(q)
	data['quantity']=res

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	print(action)
	
	if action=="request":
		q="select * from request where Stock_id='%s'"%(id)
		res=select(q)
		if res:
			flash("ALREDY REQUESTED")
			return redirect(url_for('seller.seller_view_stocks'))
		else:
			q="insert into request values (null,'%s','pending','pending')"%(id)
			insert(q)
			return redirect(url_for('seller.seller_view_stocks'))

	 	

	return render_template("seller_view_stocks.html",data=data)

@seller.route("seller_for_sell_amount",methods=['get','post'])
def seller_for_sell_amount():
	data={}
	Stock_id=request.args['Stock_id']
	q="SELECT * FROM `request` WHERE `Stock_id`='%s'"%(Stock_id)
	res=select(q)
	if res:
		data['amount']=res

	if 'add_rate' in request.form:
		amount=request.form['amount']
		q="INSERT INTO `request` VALUES(NULL,'%s','%s','For Sell')"%(Stock_id,amount)
		insert(q)
		return redirect(url_for("seller.seller_for_sell_amount",Stock_id=Stock_id))

	if 'update_rate' in request.form:
		amount=request.form['amount']
		q="UPDATE `request` SET `amount`='%s' WHERE `Stock_id`='%s'"%(amount,Stock_id)
		update(q)
		return redirect(url_for("seller.seller_for_sell_amount",Stock_id=Stock_id))


	return render_template("seller_for_sell_amount.html",data=data)

@seller.route('/seller_view_requested_auction',methods=['get','post'])
def seller_view_requested_auction():
	data={}
	selid=session['selid']
	q="SELECT * FROM stock INNER JOIN quality USING(Quality_id)INNER JOIN request USING(Stock_id) where Seller_id='%s'"%(selid)
	res=select(q)
	print(res)
	data['request_view']=res


	
	if 'action' in request.args:
		action=request.args['action']
		sid=request.args['sid']
		amt=request.args['amt']
	else:
		action=None
		print(action)

	if action=="upamt":
		q="select * from request where request_id='%s'"%(sid)
		res=select(q)
		data['up_amt']=res 

	if 'button' in request.form:
		amt=request.form['ant']
		q="update request set amount='%s' where request_id='%s'" %(amt,sid)
		update(q)
		return redirect(url_for('seller.seller_view_requested_auction',sid=sid))


	return render_template("seller_view_requested_auction.html",data=data)	


@seller.route('/seller_view_booking')
def seller_view_booking():
	data={}
	selid=session['selid']
	q="SELECT *,`booking`.`Quantity` AS bquantity FROM `booking` INNER JOIN stock USING(`Stock_id`) INNER JOIN quality USING(Quality_id) INNER JOIN USER USING(User_id) WHERE `Stock_id` IN (SELECT Stock_id FROM `stock` WHERE `Seller_id`='%s')"%(selid)
	res=select(q)
	data['booking']=res
	return render_template("seller_view_booking.html",data=data)


@seller.route('/seller_view_bidassigned',methods=['get','post'])	
def seller_view_bidassigned():
	data={}
	selid=session['selid']
	
	q="SELECT * FROM `auction`  INNER JOIN stock USING(`Stock_id`) INNER JOIN quality USING(Quality_id) WHERE auction.status='finished' and Seller_id='%s'"%(selid)
	res=select(q)
	data['auction']=res
	if 'action' in request.args:
		aid=request.args['aid']
		q="SELECT * FROM bid inner join user using(user_id) where auction_id='%s' order by(amt) desc"%(aid)
		res=select(q)
		if res:
				data['assigned']=res[0]
				data['aid']=aid
		q="select * from auctionpayment where auction_id='%s'"%(aid)
		res=select(q)
		if res:
			data['amt']=res[0]['amt']
			

	if 'action2' in request.args:
		aid=request.args['aid']	
		q="select Stock_id from auction where auction_id='%s'"%(aid)
		res=select(q)
		sid=res[0]['Stock_id']
		q="delete from request where Stock_id='%s'"%(sid)
		delete(q)
		q="delete from auction where auction_id='%s'"%(aid)
		delete(q)
		print(q)
		return redirect(url_for('seller.seller_view_bidassigned'))
	return render_template("seller_view_bidassigned.html",data=data)


@seller.route('/seller_view_rating',methods=['get','post'])
def seller_view_rating():
	data={}
	selid=session['selid']
	q="select * from rating inner join user using(user_id) where Seller_id='%s'"%(selid)
	res=select(q)
	print(res)
	data['rating']=res
	print(res)
	# q="select * from feedback inner join branches using(branch_id) where admin_id='%s'"%(cid)	
	# res=select(q)
	# data['fb']=res
	# print(res)
	return render_template('seller_view_rating.html',data=data)