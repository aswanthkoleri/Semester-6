faculty(aswanth,male,professor,ai,it).
faculty(sreejith,male,asst_professor,ai,it).
faculty(akshay,male,professor,deepLearning,it).
faculty(amrutha,female,asst_professor,deepLearning,it).
faculty(navya,female,professor,robotics,ece).
faculty(pranav,male,asst_professor,robotics,ece).
faculty(malavika,female,professor,energy,ece).
faculty(jithin,male,asst_professor,energy,ece).

hod(akshay,it).
hod(navya,ece).
hod(anand,mba).
student(student1,aswanth).
student(student2,navya).
student(student3,akshay).
student(student4,pranav).
student(student5,malavika).
student(student6,jithin).
student(student7,sreejith).
student(student8,amrutha).
student(student9,aswanth).
student(student10,navya).
student(student11,akshay).
student(student12,pranav).
student(student13,malavika).
student(student14,jithin).
student(student15,sreejith).	

isFaculty(X) :-
    faculty(X,_,Y,_,_),
    format('Yes ~w is a faculty working as ~w',[X,Y]).

facultyList :-
    faculty(X,_,_,_,_),
    format('~w ~n',[X]).

facultyType(X) :-
    faculty(X,_,Y,_,_),
    format('Department of ~w is ~w',[X,Y]).    

getAreas :-
    distinct(X,faculty(_,_,_,X,_)),
    format('Area : ~w',[X]).

getDept :-
    distinct(X,faculty(_,_,_,_,X)),
    format('Dept : ~w',[X]).
deptOf(X) :-
    faculty(X,_,_,_,Y),
    format('Department of ~w is ~w ',[X,Y]).
getHod :-
	hod(X,Y),
	format('~w, HOD of ~w ',[X,Y]).

/*isMale(X) :- 
	faculty(X,male,_,_,_).
noOfMaleFaculty :-
	aggregate_all(count,isMale(_),Count),
	format('~w is the no of male faculty ',[Count]).*/

noOfFaculty(Gender):-
	aggregate_all(count,faculty(_,Gender,_,_,_),Count),
	format('~w is the no of ~w faculties',[Count,Gender]).

noOfFaculty(FType):- 
	aggregate_all(count,faculty(_,_,FType,_,_),Count),
	format('~w is the no of ~w faculties',[Count,FType]).

studentsUnder(Fname) :- 
	student(X,Fname),
	format('~w is under ~w ',[X,Fname]).

noStudents :-
	aggregate_all(count,student(_,_),Count),
	format('~w is the no of students',[Count]).

noOfStudentUnder(Fname) :- 
	aggregate_all(count,student(_,Fname),Count),
	format('~w students are under ~w ',[Count,Fname]).

areaOfStudent(Sname):-
	student(Sname,X),
	faculty(X,_,_,Y,_),
	format('~w is the area of ~w',[Y,Sname]).

deptOfStudent(Sname):-
	student(Sname,X),
	faculty(X,_,_,_,Y),
	format('~w is the dept of ~w',[Y,Sname]).

studentIn(Dname):-
	faculty(X,_,_,_,Dname),
	student(Y,X),
	format('~w ',[Y]).

isStudentIn(Dname):-
	faculty(X,_,_,_,Dname),
	student(_,X).

noOfStudentIn(Dname):-
	aggregate_all(count,isStudentIn(Dname),Count),
	format('~w is the no of studnets in ~w',[Count,Dname]).