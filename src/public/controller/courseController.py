from fastapi import status, Response
from sqlalchemy.orm import Session

from ..config.database import Base, engine
#from ..models import courseModel
from ..models.courseModel import CourseModel
from ..schemas.course_schema import CourseCreate

#Base.metadata.create_all(bind=engine)
class CourseController:

    @staticmethod
    def get_all_courses(db: Session):
        courses = db.query(CourseModel).all()
        return courses


    @staticmethod
    def get_course_by_id(course_id: int, db: Session):
        course = db.query(CourseModel).filter_by(id_course=course_id).first()
        return course


    @staticmethod
    def create_course(course: CourseCreate , db: Session):

        new_course = CourseModel( **course.model_dump())

        db.add(new_course)
        db.commit()
        db.refresh(new_course)

        return new_course


    @staticmethod
    def delete_course(course_id: int, db: Session) -> None | Response :
        delete_course = db.query(CourseModel).filter_by(id_course=course_id)

        delete_course.delete(synchronize_session=False)
        db.commit()

        return Response(status=status.HTTP_204_NO_CONTENT)


    @staticmethod
    def update_course(course_id: int, course: CourseCreate, db: Session):
        update_course =  db.query(CourseModel).filter_by(id_course=course_id)

        update_course.update(course.model_dump())
        db.commit()

        return update_course.first()
