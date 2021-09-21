export default function getStudentIdsSum(StudentsList) {
  /* eslint-disable no-magic-numbers */
  return StudentsList.reduce(
    (total, obj) => obj.id + total,
    0
);
}
