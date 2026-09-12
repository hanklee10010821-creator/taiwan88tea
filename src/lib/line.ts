const LINE_OFFICIAL_ACCOUNT_ID = '@wgc0409f';

export function lineMessageUrl(message: string) {
  return `https://line.me/R/oaMessage/${encodeURIComponent(LINE_OFFICIAL_ACCOUNT_ID)}/?${encodeURIComponent(message)}`;
}

export const lineMessages = {
  home: '我從88茶葉網站首頁來，想請你幫我選茶',
  products: '我從88茶葉網站產品頁來，想請你幫我選茶',
  awardLishan: '我從88茶葉網站來，想問三星梨山茶',
  alishan: '我從88茶葉網站產品頁來，想問阿里山春茶',
  shanlinxi: '我從88茶葉網站產品頁來，想問杉林溪春茶',
  zhulu: '我從88茶葉網站產品頁來，想問石棹珠露',
  about: '我從88茶葉品牌介紹頁來，想請你幫我選茶',
};
