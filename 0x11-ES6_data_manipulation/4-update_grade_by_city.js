export default function getStudentIdsSum(StudentsList, city, newGrades) {
  /* eslint-disable func-names */

  const cond = function(id) {
    const stud = newGrades.find((st) => st.studentId === id);

    if (stud) {
      return stud.grade;
    }

    return null;

  };

  return StudentsList.filter((obj) => obj.location === city).map((ob) => ({
      ...ob,
      grade: cond(ob.id) || 'N/A',
    }));
}
