export default function UserRank () {
  const avatar = "https://www.gravatar.com/avatar/2c7d99fe281ecd3bcd65ab915bac6dd5?s=250"
  const address = "0x71C66...28e5E"
  const users = [{
    avatar,
    address
  },
  {
    avatar,
    address
  },
  {
    avatar,
    address
  },
  {
    avatar,
    address
  }]
  return(
    <div className="">
      <h1 className="text-xl sm:text-3xl font-bold text-center">User ranking</h1>
      <div className="my-16 bg-secondary p-8 rounded-lg divide-y-2 divide-dashed divide-primary outline outline-2 outline-primary">
        {users.map((user, index) => (
          <div className="flex h-20 justify-center sm:justify-start items-center gap-4 cursor-pointer" key={index}>
            <div>
              <img className="w-8 h-8 sm:w-12 sm:h-12 rounded-full outline outline-accent" src={user.avatar} />
            </div>
            <div>
              <p>{user.address}</p>
              <p>r tincidunt. Cras dapibus. Vivamus elementum</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}