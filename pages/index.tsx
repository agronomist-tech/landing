import Head from 'next/head';

// @ts-ignore
import {AnimatedOnScroll} from "react-animated-css-onscroll";

export default function Home() {
    return (
        <>
            <Head>
                <meta charSet="UTF-8"/>
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>
                <link rel="shortcut icon" href="/images/favicon.ico"/>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css"/>
                <title>Agronomist.tech - analytics platform</title>
            </Head>

            <header className="header">
                <div className="container">
                    <div className="header__inner">
                        <a className="header__logo" href="./">
                            <img src="/images/ic-logo.svg" alt=""/>
                        </a>
                        <div className="header__links links">
                            <a className="links__item links__item_doc" target="_blank"
                               href="/docs/agronomist.pdf">Whitepaper</a>
                            <a className="links__item links__item_grid" href="./">Launch App</a>
                        </div>
                        <div className="header__socials socials">
                            <a className="socials__item socials__item_tw" target="_blank" rel="noreferrer"
                               href="https://twitter.com/AgronomistTech"/>
                            <a className="socials__item socials__item_git" target="_blank" rel="noreferrer"
                               href="https://github.com/agronomist-tech/"/>
                            <a className="socials__item socials__item_discord" target="_blank" rel="noreferrer"
                               href="http://discord.gg/tR45QftB6K"/>
                        </div>
                    </div>
                </div>
            </header>

            <section className="hero">
                <div className="container">
                    <div className="hero__inner">
                        <div className="hero__side">
                            <h1 className="hero__title title">Agronomist</h1>
                            <p className="hero__info">Powerful DeFi analytics platform for farming, staking and
                                liqudity pools</p>
                            <div className="hero__buttons">
                                <a className="hero__button" href="./">Launch App</a>
                                <a className="hero__button" href="/docs/agronomist.pdf">Read more</a>
                            </div>
                        </div>
                        <div className="hero__image"><img src="/images/hero__image.png" alt=""/></div>
                    </div>
                </div>
            </section>


            <section className="advantages">
                <div className="container">
                    <div className="advantages__inner">
                        <h2 className="advantages__title title">Our advantages</h2>
                        <div className="advantages__items">
                            <div className="advantages__item card">
                                <AnimatedOnScroll animationIn="bounceInLeft">
                                    <h3 className="card__title">Multichain support</h3>
                                    <div className="card__content">
                                        <span>Support of all popular chains</span>
                                        <ul className="card__items">
                                            <li className="card__item card__item_sln">Solana</li>
                                            <li className="card__item card__item_bsc">BSC</li>
                                            <li className="card__item card__item_plg">Polygon</li>
                                            <li className="card__item card__item_etr">Ethereum</li>
                                        </ul>
                                    </div>
                                </AnimatedOnScroll>
                            </div>


                            <div className="advantages__item card">
                                <AnimatedOnScroll animationIn="bounceInRight">
                                    <h3 className="card__title">Smart analytics for farming</h3>
                                    <div className="card__content">
                                        <span>A many indicators for farm rating</span>
                                        <ul className="card__items">
                                            <li className="card__item card__item_chk">APY/APR</li>
                                            <li className="card__item card__item_chk">Popularity</li>
                                            <li className="card__item card__item_chk">Customer count</li>
                                            <li className="card__item">and more</li>
                                        </ul>
                                    </div>
                                </AnimatedOnScroll>
                            </div>

                            <div className="advantages__item card">
                                <AnimatedOnScroll animationIn="bounceInLeft">
                                    <h3 className="card__title">Notifications</h3>
                                    <div className="card__content">
                                        <p>User defined and pre-defined markers for early actions. Configurable backends with custom decisions</p>
                                    </div>
                                </AnimatedOnScroll>
                            </div>
                            <div className="advantages__item card">
                                <AnimatedOnScroll animationIn="bounceInRight">
                                    <h3 className="card__title">Risk assessment</h3>
                                    <div className="card__content">
                                        <p>Based on a lot of metrics for each farm, staking or liquidity pool with
                                            machine
                                            learning</p>
                                    </div>
                                </AnimatedOnScroll>
                            </div>
                            <div className="advantages__item card">
                                <AnimatedOnScroll animationIn="bounceInLeft">
                                    <h3 className="card__title">Government</h3>
                                    <div className="card__content">
                                        <p>Voting for the future features and project development</p>
                                    </div>
                                </AnimatedOnScroll>
                            </div>
                        </div>
                    </div>
                </div>
            </section>


            <section className="roadmap">
                <div className="roadmap__inner container">
                    <h2 className="roadmap__title title">Roadmap</h2>
                    <div className="roadmap__items">
                        <div className="roadmap__item roadmap__item_lamp">
                            <span>Idea</span>
                            <span>Spring 2021</span>
                        </div>
                        <div className="roadmap__item roadmap__item_community">
                            <span>Grow community</span>
                            <span>June-July 2021</span>
                        </div>
                        <div className="roadmap__item roadmap__item_chip">
                            <span>Token distribution</span>
                            <span>August 2021</span>
                        </div>
                        <div className="roadmap__item roadmap__item_hosting">
                            <span>Base features</span>
                            <span>September 2021</span>
                        </div>
                        <div className="roadmap__item roadmap__item_analytics">
                            <span>First analytics</span>
                            <span>Autumn 2021</span>
                        </div>
                        <div className="roadmap__item roadmap__item_blockchain">
                            <span>New blockchains</span>
                            <span>Winter 2021-22</span>
                        </div>
                    </div>
                    <div className="roadmap__progress"><span style={{width: "45%"}}/></div>
                </div>
            </section>

            <footer className="footer">
                <div className="container">
                    <div className="footer__inner">
                        <div className="footer__socials socials">
                            <a className="socials__item socials__item_tw" target="_blank" rel="noreferrer"
                               href="https://twitter.com/AgronomistTech"/>
                            <a className="socials__item socials__item_git" target="_blank" rel="noreferrer"
                               href="https://github.com/agronomist-tech/"/>
                            <a className="socials__item socials__item_discord" target="_blank" rel="noreferrer"
                               href="http://discord.gg/tR45QftB6K"/>
                        </div>
                        <div className="footer__links links">
                            <a className="links__item links__item_doc" href="/docs/agronomist.pdf">Whitepaper</a>
                            <a className="links__item links__item_grid" href="./">Launch App</a>
                        </div>
                        <a className="footer__logo" href="./"><img src="./images/ic-logo.svg" alt=""/></a>
                    </div>
                </div>
            </footer>
        </>
    )
}
