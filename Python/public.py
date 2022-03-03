from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():
	return render_template('home.html')

@public.route('/about')
def about():
	return render_template('about.html')	

@public.route('/contact')
def contact():
	return render_template('contact.html')		

@public.route('/login',methods=['get','post'])
def login():
	if 'log' in request.form:
		username=request.form['uname']
		password=request.form['pass']
		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)
		if res:
			session['logid']=res[0]['login_id']
			logid=session['logid']
			if res[0]['user_type']=="admin":
				return redirect(url_for('admin.adminhome'))
			if res[0]['user_type']=="seller":
				q="select * from seller where login_id='%s'"%(logid)
				res=select(q)
				if res:
					session['selid']=res[0]['Seller_id']
					selid=session['selid']
					return redirect(url_for('seller.sellerhome'))

			if res[0]['user_type']=="user":
				q="select * from user where login_id='%s'"%(logid)
				res=select(q)
				if res:
					session['byid']=res[0]['User_id']
					byid=session['byid']                                                                  
					return redirect(url_for('buyer.buyer_home'))    
		else:
			flash('INVALID USERNAME OR PASSWORD')
	return render_template('login.html')


@public.route('/user_registration',methods=['get','post'])
def user_registration():
	if 'register' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		phone=request.form['phno']
		place=request.form['pl']
		email=request.form['email']
		address=request.form['address']
		username=request.form['uname']
		password=request.form['pass']
		print(username)
		q="insert into login values(null,'%s','%s','user')" %(username,password)
		id=insert(q)

		q="insert into user values(null,'%s','%s','%s','%s','%s','%s','%s')" %(id,fname,lname,place,phone,email,address)
		insert(q)
	return render_template('user_registration.html')
	

@public.route('/seller_registration',methods=['get','post'])
def seller_registration():
	if 'register' in request.form:
		sname=request.form['sname']
		place=request.form['pl']
		phone=request.form['phno']
		email=request.form['mail']
		address=request.form['address']
		username=request.form['uname']
		password=request.form['pass']
		q="insert into login values(null,'%s','%s','pending')" %(username,password)
		id=insert(q)
		q="insert into seller values(null,'%s','%s','%s','%s','%s','%s')" %(id,sname,place,phone,email,address)
		insert(q)
	return render_template('seller_registration.html')	
		
