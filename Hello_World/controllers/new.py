def fun():
    if not session.counter:
        session.counter=1;
    else:
        session.counter+=1
    return dict(msg="Hello World",c=session.counter);
