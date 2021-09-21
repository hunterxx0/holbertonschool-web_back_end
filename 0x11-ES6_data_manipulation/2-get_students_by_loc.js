export default function getStudentsByLocation(StudentsList, city) {
  return StudentsList.filter((obj) => obj.location === city);
}
