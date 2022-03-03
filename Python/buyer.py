from flask import *
from database import *

buyer=Blueprint('buyer',__name__)
@buyer.route('/buyer_home')
def buyer_home():
	return render_template("buyer_home.html")

@buyer.route('/about')
def about():
	return render_template("about.html")

@buyer.route('/buyer_view_product')
def buyer_view_product():
	data={}
	# q="select * from stock inner join request using(Stock_id) inner join quality using(Quality_id) "
	q="SELECT * FROM stock INNER JOIN request USING(Stock_id) INNER JOIN quality USING(Quality_id) WHERE `sell_type`='Normal Sell'"
	print(q)
	res=select(q)
	data['request']=res
	return render_template("buyer_view_product.html",data=data)

@buyer.route('/buyer_book_product',methods=['get','post'])
def buyer_book_product():
	data={}
	sid=request.args['sid']
	amt=request.args['amt']
	qua=request.args['qua']
	print("+++++++++++")
	qua=qua.split('kg')[0]
	print(qua)
	data['qua']=qua
	data['amt']=amt
	if 'submit' in request.form:
		quantity=request.form['quantity']
		amount=request.form['total_amount']
		q="insert into booking values(null,'%s','%s','%s','%s',curdate())"%(sid,session['byid'],quantity,amount)
		id=insert(q)
		
		return redirect(url_for('buyer.buyer_view_booking_details',amount=amount,bid=id,qua=quantity))
	return render_template("buyer_book_product.html",data=data)


@buyer.route('/buyer_view_booking_details',methods=['get','post'])	
def buyer_view_booking_details():
	amount=request.args['amount']
	qua=request.args['qua']
	bid=request.args['bid']
	if 'submit' in request.form:

		q="insert into payment values(null,'%s','%s',curdate())"%(bid,amount)
		insert(q)
		q="select * from booking where booking_id='%s'"%(bid)
		res=select(q)
		sid=res[0]['Stock_id']
		
		q="update stock set quantity=quantity-'%s' where Stock_id='%s'"%(qua,sid)
		update(q)
		flash("booked sucessfully")
		return redirect(url_for('buyer.buyer_view_product'))
	
	return render_template("buyer_view_booking_details.html",amount=amount)


@buyer.route('/buyer_view_my_orders',methods=['get','post'])
def buyer_view_my_orders():
	data={}
	
	q="SELECT *,`booking`.`Quantity` AS bqnty,`booking`.`Amount` AS bamount FROM `booking` INNER JOIN `stock` USING(`Stock_id`) INNER JOIN `quality` USING(`Quality_id`) INNER JOIN `seller` USING(`Seller_id`) WHERE `User_id`='%s'"%(session['byid'])
	res=select(q)
	data['my_orders']=res


	return render_template("buyer_view_my_orders.html",data=data)	

@buyer.route('/buyer_send_complaint',methods=['get','post'])
def buyer_send_complaint():
	data={}
	bid=session['byid']
	if "submit" in request.form:
		complaint=request.form['complaint']
		q="insert into complaint values(null,'%s','%s','pending',curdate())"%(bid,complaint)
		insert(q)
		return redirect(url_for('buyer.buyer_send_complaint'))
	q="select * from complaint where user_id='%s'" %(bid)
	res=select(q)
	data['complaint']=res


	return render_template("buyer_send_complaint.html",data=data)	
	


@buyer.route('/buyer_view_auction',methods=['get','post'])	
def buyer_view_auction():
	data={}
	q="SELECT * FROM `auction` INNER JOIN stock USING(`Stock_id`) INNER JOIN seller USING(Seller_id) INNER JOIN quality USING(Quality_id) WHERE CURDATE() BETWEEN `auction`.`auction_date` AND `auction`.`end_date` and auction.status!='finished' AND `sell_type`='Auction'"
	print(q)
	res=select(q)
	data['auction']=res
	return render_template("buyer_view_auction.html",data=data)


@buyer.route('/buyerbid',methods=['get','post'])	
def buyerbid():
	data={}
	bid=session['byid']
	aid=request.args['aid']
	session['aid']=aid
	data={}
	q="select max(amt) as amts from bid where auction_id='%s' order by(amt)"%(aid)
	res=select(q)
	data['minamt']=res[0]['amts']
	q="SELECT * FROM bid inner join user using(user_id) where auction_id='%s' order by(amt) desc"%(aid)
	res=select(q)
	data['bid']=res
	if 'submit' in request.form:
		myamt=request.form['myamt']
		q="insert into bid values(NULL,'%s','%s','%s',NOW())"%(bid,aid,myamt)
		insert(q)
		return(redirect(url_for('buyer.buyerbid',aid=aid)))
	
	return render_template("buyerbid.html",data=data)


@buyer.route('/buyer_view_bid_assigned',methods=['get','post'])	
def buyer_view_bid_assigned():
	data={}
	bid=session['byid']
	data['bid']=bid
	q="SELECT * FROM `auction` INNER JOIN stock USING(`Stock_id`) INNER JOIN seller USING(Seller_id) INNER JOIN quality USING(Quality_id) WHERE  auction.status='finished'"
	res=select(q)
	data['auction']=res
	if 'action' in request.args:
		aid=request.args['aid']
		q="SELECT * FROM bid inner join user using(user_id) where auction_id='%s' order by(amt) desc"%(aid)
		res=select(q)
		if res:
				data['assigned']=res[0]
	if 'action2' in request.args:
		amt=request.args['amt']
		aid=request.args['aid']
		q="select * from auctionpayment where auction_id='%s'"%(aid)
		res=select(q)
		if res:
			flash("ALREADY PAID")
		else:
			data['amt']=amt
			
	if 'pay' in request.form:
		amt=request.args['amt']

		q="insert into auctionpayment values(NULL,'%s','%s',NOW())"%(aid,amt)
		insert(q)
		# q="insert into cargo_status values(NULL,'%s','pending',NOW()"%(boid)
		# insert(q)
		flash("PAYMENT SUCESS")

		return redirect(url_for('buyer.buyer_view_bid_assigned'))
		
	return render_template("buyer_view_bid_assigned.html",data=data)





@buyer.route('/buyer_view_bill',methods=['get','post'])	
def buyer_view_bill():
	data={}
	byid=session['byid']
	amt=request.args['amt']
	data['amt']=amt
	aid=request.args['aid']
	q="SELECT * FROM `auction` INNER JOIN stock USING(`Stock_id`) INNER JOIN seller USING(Seller_id) INNER JOIN quality USING(Quality_id) WHERE auction_id='%s'"%(aid)
	res=select(q)
	data['auction']=res
	q="select * from user where User_id='%s'"%(byid)
	res=select(q)
	data['userdetails']=res
	
		
	return render_template("buyer_view_bill.html",data=data)


@buyer.route('/buyer_add_rate',methods=['get','post'])
def buyer_add_rate():
	data={}
	bid=session['byid']
	q="select * from seller inner join login using(login_id) where user_type='seller'"
	res=select(q)
	data['seller']=res
	print(res)
	if 'action' in request.args:
		sid=request.args['sid']
		name=request.args['name']
		data['rate']=name
		q="select * from rating where User_id='%s' and Seller_id='%s'"%(bid,sid)
		res=select(q)
		if res:
			data['rating']=res[0]['Rated']

	if 'star-rating' in request.form:
		q="select * from rating where User_id='%s' and Seller_id='%s'"%(bid,sid)
		res=select(q)
		if res:
			rating=request.form['rating']
			q="update rating set rated='%s' where  User_id='%s' and Seller_id='%s'"%(rating,bid,sid)
			update(q)
			return redirect(url_for('buyer.buyer_add_rate',bid=bid))
		else:

			rating=request.form['rating']
			q="insert into rating values(null,'%s','%s','%s',curdate())" %(sid,bid,rating)
			insert(q)
			return redirect(url_for('buyer.buyer_add_rate',bid=bid))

	return render_template('buyer_add_rate.html',data=data)





@buyer.route('/user_bill_pdf',methods=['get','post'])	
def user_bill_pdf():
	data={}
	Booking_id=request.args['Booking_id']
	q="SELECT *,`booking`.`Quantity` AS bqnty,booking.Amount AS bamount,`user`.`Phone` AS uphone,`user`.`Email` AS uemail,`user`.`Address` as uaddress,`user`.`Place` AS uplace ,`seller`.`Place` AS splace,`seller`.`Phone` AS sphone,`seller`.`Email` AS semail,`seller`.`Address` AS saddress FROM `booking` INNER JOIN `stock` USING(`Stock_id`) INNER JOIN `quality` USING(`Quality_id`) INNER JOIN `user` USING(`User_id`) INNER JOIN `seller` USING(`Seller_id`) WHERE `Booking_id`='%s'"%(Booking_id)
	res=select(q)
	data['bill']=res
	
		
	return render_template("user_bill_pdf.html",data=data)
