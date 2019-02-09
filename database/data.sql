--
-- PostgreSQL database dump
--

-- Dumped from database version 10.5
-- Dumped by pg_dump version 10.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: render_cache_pagehtml; Type: TABLE; Schema: public; Owner: render
--

CREATE TABLE public.render_cache_pagehtml (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    page_id integer NOT NULL,
    url text NOT NULL,
    generator_url text NOT NULL,
    html text NOT NULL,
    tfn_site_id integer NOT NULL,
    is_hidden boolean NOT NULL
);


ALTER TABLE public.render_cache_pagehtml OWNER TO render;

--
-- Name: render_cache_pagehtml_id_seq; Type: SEQUENCE; Schema: public; Owner: render
--

CREATE SEQUENCE public.render_cache_pagehtml_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.render_cache_pagehtml_id_seq OWNER TO render;

--
-- Name: render_cache_pagehtml_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: render
--

ALTER SEQUENCE public.render_cache_pagehtml_id_seq OWNED BY public.render_cache_pagehtml.id;


--
-- Name: render_cache_pagehtml id; Type: DEFAULT; Schema: public; Owner: render
--

ALTER TABLE ONLY public.render_cache_pagehtml ALTER COLUMN id SET DEFAULT nextval('public.render_cache_pagehtml_id_seq'::regclass);


--
-- Data for Name: render_cache_pagehtml; Type: TABLE DATA; Schema: public; Owner: render
--

COPY public.render_cache_pagehtml (id, created, modified, page_id, url, generator_url, html, tfn_site_id, is_hidden) FROM stdin;
1	2019-01-14 17:40:09.377+03	2019-01-14 17:40:13.298+03	1	startmatter.com	startmatter.com	<html><head><title>Start Matter</title></head><body>Start Matter!</body></html>	1	f
\.


--
-- Name: render_cache_pagehtml_id_seq; Type: SEQUENCE SET; Schema: public; Owner: render
--

SELECT pg_catalog.setval('public.render_cache_pagehtml_id_seq', 1, true);


--
-- Name: render_cache_pagehtml render_cache_pagehtml_page_id_generator_url_url_ed92cdcf_uniq; Type: CONSTRAINT; Schema: public; Owner: render
--

ALTER TABLE ONLY public.render_cache_pagehtml
    ADD CONSTRAINT render_cache_pagehtml_page_id_generator_url_url_ed92cdcf_uniq UNIQUE (page_id, generator_url, url);


--
-- Name: render_cache_pagehtml render_cache_pagehtml_pkey; Type: CONSTRAINT; Schema: public; Owner: render
--

ALTER TABLE ONLY public.render_cache_pagehtml
    ADD CONSTRAINT render_cache_pagehtml_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

