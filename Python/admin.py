from flask import *
from database import *


admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
	return render_template("adminhome.html")


@admin.route('/admin_manage_quality',methods=['get','post'])
def admin_manage_quality():
	data={}
	if 'submit' in request.form:
		quality=request.form['quality']
		percent=request.form['per']
		q="insert into quality values(null,'%s','%s')" %(quality,percent)
		insert(q)
		flash("ADDED SUCESSFULLY")
		return redirect(url_for('admin.admin_manage_quality'))

	q="select *from quality"
	res=select(q)
	data['quality']=res

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None

	if action=="delete":
		q="delete from quality where Quality_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.admin_manage_quality'))

	if action == "update":
		q="select* from quality where Quality_id='%s'"%(id)
		res= select(q)
		data['updater'] = res
	if 'update' in request.form:
		quality=request.form['quality']
		percent=request.form['per']
		q= "update quality set Quality = '%s' ,percent = '%s' where Quality_id='%s' "%(quality,percent,id)
		update(q)
		return redirect(url_for('admin.admin_manage_quality'))

	return render_template("admin_manage_quality.html",data=data)




@admin.route('/admin_manage_price',methods=['get','post'])
def admin_manage_price():
	data={}
	if 'submit' in request.form:
		price=request.form['price']
		q="insert into price values(null,'%s')" %(price)
		insert(q)
		return redirect(url_for('admin.admin_manage_price'))

	q="select *from price"
	res=select(q)
	data['price']=res

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None

	if action=="delete":
		q="delete from price where price_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.admin_manage_price'))

	if action == "update":
		q="select* from price where price_id='%s'"%(id)
		res= select(q)
		data['updater'] = res
	if 'update' in request.form:
		price=request.form['price']
		q= "update price set price = '%s'  where price_id='%s' "%(price,id)
		update(q)
		return redirect(url_for('admin.admin_manage_price'))

	return render_template("admin_manage_price.html",data=data)




@admin.route('/admin_view_seller',methods=['get','post'])
def admin_view_seller():
	data={}

	if 'action' in request.args:

		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	print(action)

	if action=="block":
		q= "update login set user_type ='sellers' where login_id='%s' "%(id)
		update(q)
		return redirect(url_for('admin.admin_view_seller'))
	if action=="unblock":
		q= "update login set user_type ='seller' where login_id='%s' "%(id)
		update(q)
		return redirect(url_for('admin.admin_view_seller'))

	q="select * from seller inner join login using(login_id)"
	res=select(q)
	data['seller']=res
	
	return render_template("admin_view_seller.html",data=data)

@admin.route('/admin_manage_auction',methods=['get','post'])
def admin_manage_auction():
	data={}
	sid=request.args['Stock_id']
	
	amt=request.args['amt']
	# amt=int(amt)*int(quan)
	data['amt']=amt
	if 'submit' in request.form:
		
		amt=request.form['amt']
		date=request.form['date']
		edate=request.form['edate']
		q="insert into auction values(null,'%s','%s','%s','%s','pending')" %(sid,amt,date,edate)
		aid=insert(q)
		
		q="UPDATE `request` SET amount='%s',STATUS='accept' WHERE Stock_id='%s' "%(amt,sid)
		print(q)
		update(q)
		q="insert into bid values(NULL,'0','%s','%s','%s')"%(aid,amt,date)
		insert(q)
		flash("ACCEPTED")
		
		return redirect(url_for('admin.admin_view_request_auction'))

	# q="select *from quality"
	# res=select(q)
	# data['quality']=res

	# q="select * from auction inner join quality using(quality_id)"
	# res=select(q)
	# data['auction']=res

	# if 'action' in request.args:
	# 	action=request.args['action']
	# 	id=request.args['id']
	# else:
	# 	action=None

	# if action=="delete":
	# 	q="delete from auction where auction_id='%s'"%(id)
	# 	delete(q)
	# 	return redirect(url_for('admin.admin_manage_auction'))

	# if action == "update":
	# 	q="select* from auction where auction_id='%s'"%(id)
	# 	res= select(q)
	# 	data['updater'] = res
	# if 'update' in request.form:
	# 	price=request.form['Price_id']
	# 	q= "update price set price = '%s'  where price_id='%s' "%(price,id)
	# 	update(q)
	# 	return redirect(url_for('admin.admin_manage_price'))

	return render_template("admin_manage_auction.html",data=data)

@admin.route('/admin_view_request_auction')
def admin_view_request_auction():
	data={} 
	q="select * from quality inner join stock using(Quality_id) inner join seller using(Seller_id) inner join request using(Stock_id) "
	res=select(q)
	print(res)
	data['request']=res
	
	if 'action' in request.args:
		action=request.args['action']
		sid=request.args['id']
		percent=request.args['percent']
	else:
		action=None

	if action=="reject":
		q="update request set status='reject' where Stock_id='%s'"%(sid)
		update(q)
		return redirect(url_for('admin.admin_view_request_auction'))
	if action=='accept':
		q="select * from stock where Stock_id='%s'"%(sid)
		res=select(q)
		quan=res[0]['Quantity']
		q="SELECT * FROM `price` ORDER BY price_id DESC LIMIT 1"
		res=select(q)
		print(res)
		print(res[0])
		price=res[0]['Price']
		print(price)

		amt=(int(percent)/100)*int(price)
		amt=amt*int(quan)
		print(amt)
		return redirect(url_for('admin.admin_manage_auction',Stock_id=sid,amt=amt))

	if action=="stop":
		q="update auction set status='finished' where Stock_id='%s'"%(sid)
		update(q)
		q="update request set status='finished' where Stock_id='%s'"%(sid)
		update(q)
		return redirect(url_for('admin.admin_view_request_auction'))
		# print(amt)
		
		# return redirect(url_for('admin.admin_view_request_auction'))



		
	return render_template("admin_view_request_auction.html",data=data)


@admin.route('/admin_view_complaint',methods=['get','post'])
def admin_view_complaint():
	data={}
	q="select * from complaint"
	res=select(q)
	data['complaints']=res


	j=0
	for i in range(1,len(res)+1):
		if 'replys'+str(i) in request.form:
			reply=request.form['reply'+str(i)]
			print(res[j]['Complaint_id'])
			q="update complaint set replay='%s' where complaint_id='%s'"%(reply,res[j]['Complaint_id'])
			print(q)
			update(q)
			return redirect(url_for('admin.admin_view_complaint'))
		j=j+1


	return render_template("admin_view_complaint.html",data=data)
	
