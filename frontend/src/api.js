const COOKIE_EXPIRED_MSG = 'Token has expired'
authService.interceptors.response.use((response) => {
  return response
}, async (error) => {
  const error_message = error.response.data.msg
  switch (error.response.status) {
    case 401:
      if (!error.config.retry && error_message === COOKIE_EXPIRED_MSG) {
        error.config.retry = true
        authService.defaults.xsrfCookieName = 'csrf_refresh_token';
        await authService.post('/refresh_token')
        authService.defaults.xsrfCookieName = 'csrf_access_token';
        return authService(error.config)
      }
      break;
    case 404:
      router.push('/404');
      break;
    default:
      break;
  }
  return error.response;
});