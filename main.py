from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import engine,SessionLocal

#create table 
models.Base.metadata.create_all(bind=engine)

# create FastAPI all
app=FastAPI()

#Database dependecy
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Home api
@app.get("/")
def home():
    return {
        "message":"Blog API is running......!!!!!"
    }

#Add Blog
@app.post("/addBlog",response_model=schemas.BlogResponse)
def addBlog(blog:schemas.BlogCreate,db:Session=Depends(get_db)):
    newBlog=models.Blog(
        title=blog.title,
        content=blog.content,
        author=blog.author
    )
    db.add(newBlog)
    db.commit()
    db.refresh(newBlog)

    return newBlog;

# get all blogs
@app.get("/getBlogs",response_model=list[schemas.BlogResponse])
def getBlogs(db:Session=Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs

#get blog by id
@app.get("/blog/{id}",response_model=schemas.BlogResponse)
def getBlogByID(id:int,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()

    if blog is None:
        raise HTTPException(status_code=404,detail="Blog Not Found")
    
    return blog

#update blog by id
@app.put("/updateBlog/{id}",response_model=schemas.BlogResponse)
def updateBlog(id:int,new_blog:schemas.BlogUpdate,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()

    if blog is None:
        raise HTTPException(status_code=404,detail="Blog Not Found")
    
    blog.title=new_blog.title
    blog.content=new_blog.content
    blog.author=new_blog.author

    db.commit()
    db.refresh(blog)
    
    return blog

# delete blog
@app.delete("/deleteBlog/{id}")
def delBlog(id:int,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()

    if blog is None:
        raise HTTPException(status_code=404,detail="Blog Not Found")
    
    db.delete(blog)
    db.commit()

    return {
        "message":"Blog Deleted Successfully.....!!!!"
    }