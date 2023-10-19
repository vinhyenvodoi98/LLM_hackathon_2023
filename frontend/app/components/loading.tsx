export default function Loading() {
  return(
    <dialog id="loading-modal" className="modal">
      <div className="modal-box">
      <form method="dialog">
        <button className="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>
      </form>
        <h3 className="font-bold text-lg text-center">Loading!</h3>
        <div className="flex justify-center">
          <span className="loading loading-infinity loading-lg"></span>
        </div>
      </div>
    </dialog>
  )
}
