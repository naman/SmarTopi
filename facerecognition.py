from fbrecog import recognize
path = "/Users/udayantandon/Desktop/Coala-Bof.png"
access_token = "EAACEdEose0cBAF2LiQE6mNG8ixIvblmwHwlhAwjo7tOas1ahfXlGUpLsJkQWq5iq3ENkEojFtKC5xEUSQsjzzlHtZBqPHS26eWWaxvojMrAowmNVLPFXtS8MbnXsKDrCU4rMVNzRSFwkFXqoIpo1FuL4tmAREZANB6oGbcsAZDZD"
cookie = "datr=fPqQVfDF5cEMKwcywPvt70jN; _ga=GA1.2.1788536487.1437330029; locale=en_GB; sb=_U0HV7uSQVX_Z8Oov3bZav9c; pl=n; lu=giTXKkQ81PDlziOlnp5_5J7A; c_user=100000601825742; xs=204%3As6GCwRc3trP-_w%3A2%3A1479817217%3A5827; fr=0J8CbTl5k918hSbLX.AWWGwk7QSJhzwUuSO-iL8J2fpEo.BVkPqC.Nv.Fg0.0.0.BYPH2T.AWXxfm--; csm=2; s=Aa7PrE1w24FGNzCh.BYNDgB; p=-2; presence=EDvF3EtimeF1480361527EuserFA21B00601825742A2EstateFDt2F_5b_5dElm2FnullEuct2F1480325937BEtrFA2loadA2EtwF2218223787EatF1480361522186G480361527040CEchFDp_5f1B00601825742F15CC; act=1480361603300%2F10; wd=1466x536"
fb_dtsg = "AQGQIXXXTjK_:AQH9HojIEPNb"

print(recognize(path,access_token,cookie,fb_dtsg))