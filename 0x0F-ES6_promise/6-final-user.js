import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const res = [];
  try {
    res.push({
      status: 'fulfilled',
      value: (await signUpUser(firstName, lastName)),
    });
    await uploadPhoto(fileName);
  } catch (error) {
    res.push({
      status: 'rejected',
      value: error.toString(),
    });
  }
  return res;
}
