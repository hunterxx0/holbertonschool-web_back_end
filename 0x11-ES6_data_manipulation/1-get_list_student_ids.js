export default function getListStudentIds(StudentsList) {
  const res = [];

  if (Array.isArray(StudentsList) && StudentsList.length) {
    return StudentsList.map((obj) => obj.id);
  }

return res;
}
